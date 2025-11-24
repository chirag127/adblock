# GitHub Actions Workflows

This directory contains automated workflows for the repository.

## Workflows

### 1. Ruff Lint and Format (`ruff.yml`)

**Trigger:** Push to `main` or Pull Requests to `main`

This workflow checks code quality using Ruff:

-   Runs linting checks to catch code issues
-   Verifies code formatting compliance
-   Fails if any issues are found

**Purpose:** Ensures all code meets quality standards before merging.

### 2. Ruff Auto-fix (`ruff-autofix.yml`)

**Trigger:** Push to `main` or Pull Requests to `main`

This workflow automatically fixes code issues:

-   Applies auto-fixable lint rules
-   Formats code according to Ruff standards
-   Commits and pushes changes automatically

**Purpose:** Automatically maintains code quality without manual intervention.

### 3. Make Without Domains (`make_without_domains.yml`)

**Trigger:** Scheduled daily at 12:35 UTC

This workflow generates filter lists without domain rules:

-   Fetches latest AdGuard and other filter lists
-   Removes domain-only rules
-   Commits updated filter files

**Purpose:** Keeps filter lists up-to-date automatically.

### 4. Make All Rules for Popular Sites (`make_all_rules_for_popular_sites.yml`)

**Trigger:** Scheduled daily at 3:35 UTC

This workflow generates site-specific filter rules:

-   Extracts rules for popular websites
-   Combines rules from multiple sources
-   Commits updated rule files

**Purpose:** Maintains comprehensive site-specific blocking rules.

### 5. Pylint (`pylint.yml`)

**Trigger:** Push to any branch

This workflow runs Pylint on all Python files:

-   Analyzes code for errors and style issues
-   Provides detailed code quality reports

**Purpose:** Additional code quality checks using Pylint.

## Local Development

### Running Ruff Locally

Install Ruff:

```bash
pip install ruff
```

Check for issues:

```bash
ruff check .
```

Auto-fix issues:

```bash
ruff check . --fix
```

Format code:

```bash
ruff format .
```

Check formatting without changes:

```bash
ruff format --check .
```

### Configuration

Ruff is configured via `ruff.toml` in the repository root. Key settings:

-   Line length: 88 characters (Black-compatible)
-   Target Python version: 3.10
-   Enabled rules: Pyflakes, pycodestyle, isort, pyupgrade, flake8-bugbear, flake8-simplify

## Troubleshooting

If a workflow fails:

1. Check the workflow logs in the Actions tab
2. Run the same commands locally to reproduce the issue
3. Fix the issues and push again
4. The auto-fix workflow may resolve some issues automatically
