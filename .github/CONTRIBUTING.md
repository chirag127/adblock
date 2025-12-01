# 🤝 Contributing to AdFilterCore-List-Management-Python-Lib

This repository adheres to the highest standards of software engineering, following the Apex Technical Authority mandate for Zero-Defect, Future-Proof code. We welcome contributions that uphold these principles.

## 1. CORE PRINCIPLES (The Apex Mandate)

All contributions must align with the following architectural tenets:

*   **SOLID Compliance:** Adherence to Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion principles is mandatory for new features or substantial refactors.
*   **Python Best Practices (PEP 8/9):** Strict adherence to Python standards, enforced by **Ruff** linting. Code must be clean, idiomatic, and self-documenting.
*   **Test Coverage:** New features **MUST** be accompanied by comprehensive unit and integration tests achieving 100% path coverage for the modified logic.
*   **Immutability & Predictability:** Favor pure functions over side effects. Filter list transformations must be deterministic.

## 2. DEVELOPMENT ENVIRONMENT SETUP

To ensure consistency across contributor environments, use the following setup:

1.  **Fork & Clone:** Fork the repository and clone your fork locally.
    ```bash
    git clone https://github.com/YOUR_USERNAME/AdFilterCore-List-Management-Python-Lib.git
    cd AdFilterCore-List-Management-Python-Lib
    ```

2.  **Environment Management (using `uv`):** Create and activate a dedicated virtual environment.
    ```bash
    uv venv
    source .venv/bin/activate  # Linux/macOS
    .venv\Scripts\activate    # Windows
    ```

3.  **Install Dependencies (Development & Testing):**
    ```bash
    uv pip install -e .[dev]
    ```

4.  **Pre-Commit Hooks (Mandatory):** Install pre-commit hooks managed by `pre-commit` to enforce formatting and basic linting before committing.
    ```bash
    pip install pre-commit
    pre-commit install
    ```

## 3. THE CONTRIBUTION WORKFLOW

Follow this sequence for all submissions:

### A. Branching Strategy

Create a feature or fix branch based on the latest `main` branch. Use **Conventional Commits**.

*   **Feature:** `feat/short-description` (e.g., `feat/implement-geo-blocking-logic`)
*   **Fix:** `fix/short-description` (e.g., `fix/crash-on-empty-datasource`)
*   **Refactor:** `refactor/description`

### B. Code Implementation & Verification

1.  **Develop:** Implement your feature or fix, ensuring all new code is covered by tests.
2.  **Format & Lint (Local Check):** Run the auto-fixers. This should pass before committing.
    ```bash
    ruff check --fix ./src
    black ./src
    ```
3.  **Test Execution (Mandatory Gate):** All tests must pass successfully.
    ```bash
    pytest
    ```
4.  **Documentation:** Update `README.md` if the public API changes, and update internal documentation (docstrings) as necessary.

### C. Commit and Pull Request (PR)

1.  **Commit Locally:** Use the Conventional Commit format (e.g., `feat: add support for advanced wildcards in source ingestion`).
    ```bash
    git add .
    git commit -m "feat: Implemented deterministic deduplication algorithm for filter merging"
    ```
2.  **Push:** Push your branch to your fork.
    ```bash
    git push origin feat/deduplication-logic
    ```
3.  **Open PR:** Create a Pull Request targeting the `main` branch of the upstream repository. Ensure you reference any associated issues using keywords (e.g., `Fixes #123`).

## 4. PULL REQUEST TEMPLATE & REVIEW

Your PR must be fully detailed. Use the provided `PULL_REQUEST_TEMPLATE.md` as a guide.

**The Review Process:**

*   All PRs trigger an automated CI/CD pipeline (`.github/workflows/ci.yml`). **Do not request a manual review until CI has passed.**
*   Maintainers will review against the Apex standards (SOLID, Testing, Performance).
*   Expect constructive feedback focused on architectural elegance and long-term maintainability.

## 5. SECURITY AND DEPENDENCY MANAGEMENT

*   **Dependency Updates:** Do not manually bump versions in `pyproject.toml` unless strictly necessary. Rely on automated tooling (`renovate` or equivalent in CI) for routine dependency upgrades.
*   **Security Disclosure:** If you discover a potential security vulnerability, follow the process outlined in `.github/SECURITY.md`. **Do not disclose publicly before coordination.**

Thank you for helping us maintain the integrity and performance of the AdFilterCore ecosystem!