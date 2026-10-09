# Known Misses — B2B Service Business Blog Pipeline (Template)

A running log of quality issues that slipped through the pipeline. Purpose: build guardrails from **real, repeated** failures instead of guesses.

> Template note: this is the shared B2B template. When cloning to a client vertical, carry this file over empty so each project keeps its own miss log.

## How to use this

1. **First time** you catch something off in a draft — fix it by hand and log one line below.
2. **Second time** the same kind of miss shows up — that's the signal to harden it: add a prompt rule (in the relevant `instructions/0X-*.md`), a `scripts/qc.sh` check, or a reference rule, then move the row to "Codified."
3. Two strikes, then automate. Don't build a guardrail for a one-off.

## Open misses (logged, not yet codified)

| Date | Stage | What slipped through | Draft / slug | Notes |
|------|-------|----------------------|--------------|-------|
|      |       |                      |              |       |

## Codified (fixed in prompts/scripts)

| Date | What it was | How it's now caught | Where (file) |
|------|-------------|---------------------|--------------|
|      |             |                     |              |
