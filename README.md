# Codex Auto Fix Repo

This is a mini repo with some visuals on how Codex and github actions can help you modify code in a repo. 
This is not meant to be a fully functioning repo, but rather a sandbox for you to play around with.

## Prerequisites
- Python 3.11+
- uv installed locally
- Codex CLI installed locally
- For GitHub Actions auto-fix: set repo secret `OPENAI_API_KEY`

## Running Locally
From repo root:

```bash
uv sync
uv run pytest -q
```
---

### Running Local Auto-Fix
If tests are failing, you can fix them locally by using the next command on the Codex CLI:

```
Fix failing CI by making `uv run pytest -q` pass.

Rules:
- Do NOT modify files under `tests/`
- Prefer minimal diffs
- Keep existing function signatures

Steps:
1) Run tests: `uv run pytest -q`
2) Read failures and determine root cause
3) Patch only `src/` code
4) Re-run `uv run pytest -q` until green

When done:
- Summarize what changed
- List the commands you ran
```

### Running Github Actions Auto-Fix
If your changes on a PR break the tests, you can run the same Codex prompt as above in the Github Actions workflow. 
This will create a new commit with the necessary fixes to make the tests pass.

## Grading
The changes on the PR are graded on a 100 base metric:
- 60 points for making the tests pass
- 20 points for minimal diffs (not changing more than 80 lines per PR)
- 20 points for keeping the integrity of the tests
