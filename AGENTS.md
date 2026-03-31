# Repository Guidelines

## Project Structure & Module Organization
This repository is currently minimal and root-based.
- `package.json`: Node project manifest (currently no scripts or dependencies).
- `package-lock.json`: npm lockfile for reproducible installs.
- `test.py`: placeholder Python file.

When adding production code, prefer:
- `src/` for application modules.
- `tests/` for automated tests.
- `assets/` for static files (images, fixtures, sample data).

Keep modules focused and small. Group related functionality by feature, not by file type alone.

## Build, Test, and Development Commands
There is no build pipeline configured yet. Use these baseline commands:
- `npm install`: install/update dependencies from `package.json` and lockfile.
- `npm run <script>`: run project scripts once they are added (none exist today).
- `python -m pytest`: run Python tests after `pytest` and test files are added.

If you introduce a new toolchain, add scripts to `package.json` and document them in this file.

## Coding Style & Naming Conventions
Use consistent style per language:
- JavaScript/TypeScript: 2-space indentation, `camelCase` for variables/functions, `PascalCase` for classes.
- Python: 4-space indentation, `snake_case` for functions/files, `PascalCase` for classes.
- Filenames: prefer descriptive names (`user-service.js`, `test_auth_flow.py`).

No formatter or linter is configured yet. If you add one (for example `prettier`, `eslint`, or `ruff`), include configuration files and runnable scripts.

## Testing Guidelines
A formal test framework is not configured yet.
- Place tests under `tests/` when possible.
- Python tests: `test_*.py`.
- Node tests: `*.test.js` or `*.spec.js`.
- Add tests for every behavior change and bug fix.

Prefer deterministic tests with clear setup and assertions.

## Commit & Pull Request Guidelines
Git history is not available in this workspace, so conventions are not inferable from prior commits. Use:
- Commit format: `type(scope): short summary` (for example, `feat(auth): add token validator`).
- Keep commits focused and reviewable.
- PRs should include: purpose, key changes, test evidence, and linked issue/task.
- Include screenshots only for UI-visible changes.

## Security & Configuration Tips
- Do not commit secrets or tokens.
- Keep environment-specific values in local env files (for example, `.env`) and provide a sanitized `.env.example` when needed.
- Commit lockfile updates with dependency changes.
