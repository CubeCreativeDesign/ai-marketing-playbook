# Contributing

Issues and pull requests are welcome.

## Before you open a pull request

1. Run the checks:
   ```bash
   shellcheck -S warning scripts/*.sh
   python3 -m py_compile scripts/*.py cover-generator/scripts/*.py
   scripts/doctor.sh
   ```
2. If you changed a QC script, run it on a sample draft:
   `bash scripts/qc.sh path/to/draft.md`.
3. If you changed an instruction or reference file, bump `VERSION`, add a dated
   entry to `CHANGELOG.md`, and say which stages it affects.
4. Never commit client work, API keys, `.env`, or anything under `logs/`,
   `posts/`, `output/`, `research/` or `inputs/`. The `.gitignore` covers these,
   so `git status` should never list them.

## Keep it generic

This is a template. Use placeholders such as `[YOUR_AGENCY]` and `[YOUR_VERTICAL]`
instead of a real company, client, person or city. Examples should be clearly
fictional.

## Shell scripts

- Target bash 3.2 (the macOS default) and Linux. No `mapfile`, no associative
  arrays, no GNU-only flags.
- Guard empty arrays under `set -u`: `${ARR[@]+"${ARR[@]}"}`.
- Pass values to Python as arguments or environment variables, never by pasting
  them into the Python source.
