# 🤝 Contributing to AdGuard-FilterList-Management-Python-Lib

We welcome contributions to elevate this Python library for professional AdGuard filter list management. As an Apex Authority project, we adhere to **Zero-Defect, High-Velocity, Future-Proof** engineering standards, as detailed in our `AGENTS.md`.

## 1. CORE PRINCIPLES

Before submitting, ensure your contributions align with the project's core architectural tenets:

1.  **SOLID Compliance:** New features must demonstrate clear adherence to Single Responsibility and Open/Closed Principles.
2.  **DRY Enforcement:** Avoid repetition. Refactor common logic into reusable utilities.
3.  **YAGNI Precedent:** Only build what is explicitly needed now. Avoid premature generalization.
4.  **Apex Toolchain Usage:** All development must utilize the mandated 2025/2026 Python stack: `uv` for dependency management, `Ruff` for linting/formatting, and `Pytest` for unit verification.

## 2. THE CONTRIBUTION WORKFLOW

Follow these steps for a smooth review process:

### Step 1: Fork the Repository

Create your own fork of `chirag127/AdGuard-FilterList-Management-Python-Lib` to work in isolation.

### Step 2: Clone and Configure

Clone your fork locally and ensure your environment is set up according to development standards. Always work within a dedicated feature branch.

bash
git clone https://github.com/YOUR_USERNAME/AdGuard-FilterList-Management-Python-Lib.git
cd AdGuard-FilterList-Management-Python-Lib

# Create and switch to a descriptive feature branch
git checkout -b feature/descriptive-name-of-change

# Ensure environment is set up using uv
python -m venv .venv
# Assuming uv is installed globally or via pipx
uv install -e .


### Step 3: Implement Changes

Develop your feature or fix. Crucially, all new or modified code paths **MUST** be accompanied by corresponding **Pytest** unit tests that achieve high code coverage.

### Step 4: Local Verification (The CI Pre-Flight Check)

Before pushing, run the local verification suite. This simulates the GitHub Actions CI pipeline and ensures zero failures upon submission.

bash
# Run linting and formatting check (Ruff)
ruff check .
ruff format --check .

# Run all unit tests (Pytest)
pytest

# For comprehensive checks (optional, if required by existing CI)
python -m mypy --strict


### Step 5: Commit and Push

Use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) for clear, atomic commits. Ensure the commit message clearly indicates the scope (e.g., `feat: add deduplication algorithm`, `fix: correct malformed whitelist handling`).

bash
git add .
git commit -m "type(scope): subject line"
git push origin feature/descriptive-name-of-change


### Step 6: Open a Pull Request (PR)

Navigate to the original repository (`https://github.com/chirag127/AdGuard-FilterList-Management-Python-Lib`) and open a new Pull Request from your branch against `main`.

*   **Templates:** You **MUST** use the provided `PULL_REQUEST_TEMPLATE.md` to structure your description.
*   **Verification:** The automated CI pipeline will run security scans, linting, and testing. Do not submit PRs that fail these automated checks.

## 3. ISSUE REPORTING & SECURITY

*   **Bugs:** Use the `bug_report.md` template within `.github/ISSUE_TEMPLATE/` for standardized reporting.
*   **Security:** Report all potential vulnerabilities privately via the guidelines in `.github/SECURITY.md` before disclosing publicly.

## 4. LICENSE ACKNOWLEDGEMENT

By submitting code, you agree that your contributions are licensed under the terms specified in the repository's `LICENSE` file (**CC BY-NC 4.0**).