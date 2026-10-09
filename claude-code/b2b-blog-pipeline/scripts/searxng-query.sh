#!/usr/bin/env bash
# ============================================================================
# searxng-query.sh - SearXNG metasearch wrapper for Stage 0 (optional)
# ============================================================================
# Free, unlimited, self-hosted metasearch (Google, Bing, DuckDuckGo and more in
# one query). Use it for broad URL discovery without spending Exa or Tavily
# credits. The SearXNG MCP alone is enough for Stage 0; this script is for
# shell use and for a Stage 0 run that has no SearXNG MCP.
#
# Usage:
#   scripts/searxng-query.sh "commercial cleaning marketing benchmarks 2026"
#   scripts/searxng-query.sh --num 20 "b2b service lead generation trends"
#   scripts/searxng-query.sh --json "local seo for service businesses"   # raw JSON
#   scripts/searxng-query.sh --file /path/to/query.txt
#   echo "query" | scripts/searxng-query.sh --stdin
#
# On success: prints results to stdout, exits 0
# On failure: prints the error to stderr, exits 1 (the caller falls back)
# Logs to $BLOG_LOG_DIR/searxng.log (default: <repo>/logs/searxng.log)
#
# Environment:
#   SEARXNG_URL          default http://localhost:8888
#   SEARXNG_COMPOSE_DIR  folder with the docker-compose.yml to start when SearXNG
#                        is down (default: <repo>/services/searxng). Set it to
#                        an empty value to never start anything.
# ============================================================================
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# --- Configuration ---
SEARXNG_URL="${SEARXNG_URL:-http://localhost:8888}"
COMPOSE_DIR="${SEARXNG_COMPOSE_DIR-$SCRIPT_DIR/../services/searxng}"
LOG_FILE="${BLOG_LOG_DIR:-$SCRIPT_DIR/../logs}/searxng.log"
TIMEOUT_SECONDS=30
MAX_RETRIES=2
DOCKER_WAIT=60               # wait for the Docker daemon to come up
SEARXNG_WAIT=30              # wait for the container to answer
NUM_RESULTS=10
RAW_JSON=0

mkdir -p "$(dirname "$LOG_FILE")"

log() { echo "$(date '+%Y-%m-%d %H:%M:%S') | $1" >> "$LOG_FILE"; }

# --- Parse flags + read query from args / file / stdin ---
QUERY=""
while [ $# -gt 0 ]; do
    case "$1" in
        --json)  RAW_JSON=1; shift ;;
        --num)
            if [ $# -lt 2 ] || ! [[ "$2" =~ ^[0-9]+$ ]]; then
                echo "ERROR: --num needs a whole number" >&2; exit 1
            fi
            NUM_RESULTS="$2"; shift 2 ;;
        --file)
            if [ $# -lt 2 ] || [ ! -f "$2" ]; then
                echo "ERROR: --file needs an existing file" >&2; exit 1
            fi
            QUERY=$(cat "$2"); shift 2 ;;
        --stdin) QUERY=$(cat); shift ;;
        *)       QUERY="$QUERY $1"; shift ;;
    esac
done
QUERY=$(echo "$QUERY" | sed -e 's/^ *//' -e 's/ *$//')

if [ -z "$QUERY" ]; then
    echo "ERROR: No query provided" >&2
    echo "Usage: searxng-query.sh [--json] [--num N] \"your query\"" >&2
    exit 1
fi
QUERY_PREVIEW="${QUERY:0:80}"

# --- Health check ---
check_searxng() {
    local code
    code=$(curl -s -o /dev/null -w "%{http_code}" --max-time 5 "$SEARXNG_URL/" 2>/dev/null)
    [ "$code" = "200" ]
}

# --- Bring the stack up if it is down (Docker daemon + container) ---
start_searxng() {
    log "RESTART | SearXNG not responding, attempting to bring the stack up"

    if [ -z "$COMPOSE_DIR" ] || [ ! -f "$COMPOSE_DIR/docker-compose.yml" ]; then
        log "RESTART | skipped - no docker-compose.yml at '${COMPOSE_DIR}'"
        return 1
    fi
    if ! command -v docker >/dev/null 2>&1; then
        log "RESTART | skipped - docker is not installed"
        return 1
    fi

    # 1) Make sure the Docker daemon is running
    if ! docker info >/dev/null 2>&1; then
        echo "Docker daemon not running, trying to start it..." >&2
        if command -v open >/dev/null 2>&1 && [ "$(uname -s)" = "Darwin" ]; then
            open -a Docker 2>/dev/null || true     # Docker Desktop on macOS
        fi                                         # on Linux, start dockerd with your service manager
        local waited=0
        while [ $waited -lt $DOCKER_WAIT ]; do
            sleep 3; waited=$((waited + 3))
            docker info >/dev/null 2>&1 && break
        done
        if ! docker info >/dev/null 2>&1; then
            log "RESTART | FAILED - Docker daemon did not start after ${DOCKER_WAIT}s"
            return 1
        fi
    fi

    # 2) Bring up the SearXNG container
    if ! ( cd "$COMPOSE_DIR" && docker compose up -d >>"$LOG_FILE" 2>&1 ); then
        log "RESTART | FAILED - docker compose up returned an error (see above)"
        return 1
    fi

    # 3) Wait for it to answer
    local waited=0
    while [ $waited -lt $SEARXNG_WAIT ]; do
        sleep 3; waited=$((waited + 3))
        if check_searxng; then
            log "RESTART | SearXNG is back up after ${waited}s"
            return 0
        fi
    done
    log "RESTART | FAILED - SearXNG did not answer after ${SEARXNG_WAIT}s"
    return 1
}

ensure_searxng() {
    check_searxng && return 0
    echo "SearXNG not responding, attempting restart..." >&2
    start_searxng
}

# --- Make the query (GET /search?q=...&format=json) ---
query_searxng() {
    local response_file start_time http_code end_time duration
    response_file=$(mktemp)
    start_time=$(date +%s)

    http_code=$(curl -s -G -w "%{http_code}" --max-time "$TIMEOUT_SECONDS" \
        -o "$response_file" \
        "$SEARXNG_URL/search" \
        --data-urlencode "q=$QUERY" \
        --data-urlencode "format=json" \
        --data-urlencode "safesearch=0" 2>/dev/null)

    end_time=$(date +%s); duration=$((end_time - start_time))

    if [ "$http_code" != "200" ]; then
        log "FAIL | HTTP $http_code | ${duration}s | $QUERY_PREVIEW"
        rm -f "$response_file"
        return 1
    fi

    local result
    result=$(NUM="$NUM_RESULTS" RAW="$RAW_JSON" RESPONSE_FILE="$response_file" python3 -c "
import sys, json, os
try:
    data = json.load(open(os.environ['RESPONSE_FILE']))
except Exception as e:
    print(f'Parse error: {e}', file=sys.stderr); sys.exit(1)
results = data.get('results', [])
if not results:
    print('No results', file=sys.stderr); sys.exit(1)
if os.environ.get('RAW') == '1':
    print(json.dumps(data, indent=2, ensure_ascii=False)); sys.exit(0)
n = int(os.environ.get('NUM', '10'))
for i, r in enumerate(results[:n], 1):
    title = r.get('title', '').strip()
    url = r.get('url', '').strip()
    content = ' '.join((r.get('content') or '').split())
    engines = ','.join(r.get('engines', []))
    print(f'{i}. {title}')
    print(f'   {url}')
    if content:
        print(f'   {content}')
    if engines:
        print(f'   [engines: {engines}]')
    print()
sys.exit(0)
" 2>/dev/null)

    local parse_exit=$?
    rm -f "$response_file"

    if [ $parse_exit -eq 0 ] && [ -n "$result" ]; then
        log "OK | ${duration}s | ${NUM_RESULTS} max | $QUERY_PREVIEW"
        echo "$result"
        return 0
    fi
    log "FAIL | empty/unparseable | ${duration}s | $QUERY_PREVIEW"
    return 1
}

main() {
    if ! ensure_searxng; then
        echo "ERROR: Cannot reach SearXNG and restart failed" >&2
        log "ABORT | SearXNG unreachable after restart | $QUERY_PREVIEW"
        exit 1
    fi

    local attempt=0
    while [ $attempt -le $MAX_RETRIES ]; do
        if [ $attempt -gt 0 ]; then
            log "RETRY | attempt $((attempt + 1)) of $((MAX_RETRIES + 1)) | $QUERY_PREVIEW"
            sleep 3
            ensure_searxng || { echo "ERROR: SearXNG died during retries" >&2; exit 1; }
        fi
        query_searxng && exit 0
        attempt=$((attempt + 1))
    done

    echo "ERROR: SearXNG failed after $((MAX_RETRIES + 1)) attempts" >&2
    log "ABORT | all attempts failed | $QUERY_PREVIEW"
    exit 1
}

main
