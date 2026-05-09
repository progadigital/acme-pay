# Lens Ignore Policy

Acme Pay includes a root `.lensignore` file to demonstrate how a repository can keep Lens focused on useful source, docs, tests, and operational context.

## How It Works

`.lensignore` uses `.gitignore`-style glob patterns. Files can remain committed to Git while being excluded from Lens indexing and retrieval.

## Current Ignores

| Pattern | Reason |
| --- | --- |
| `fixtures/noisy-provider-dumps/` | Repeated provider payload exports are noisy and can drown out real architecture and code signals. |
| `.pytest_cache/`, `.ruff_cache/`, `htmlcov/`, `coverage.xml` | Local tool output should not appear in answers. |
| `dist/`, `build/`, `*.egg-info/` | Generated package artifacts are reproducible and low-value for codebase questions. |

## Demo Prompt

Ask: "Why is `fixtures/noisy-provider-dumps/` excluded from Lens?"

A strong answer should mention the root `.lensignore`, the noisy provider dump fixture, and the goal of preventing repeated raw payloads from crowding out source and docs during retrieval.

