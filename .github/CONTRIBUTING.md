# Contributing to AdGuard-FilterList-Manager-Python-Lib

We welcome contributions to the AdGuard-FilterList-Manager-Python-Lib project! This project adheres to the Apex Technical Authority standards, prioritizing **Zero-Defect, High-Velocity, Future-Proof** development. Please review these guidelines to ensure your contributions align with our architectural principles and quality standards.

## 1. Code of Conduct

This project follows the Contributor Covenant Code of Conduct (v2.1). By participating, you are expected to uphold this code. Please report unacceptable behavior to [your-contact-email@example.com](mailto:your-contact-email@example.com).

## 2. Contribution Workflow

We use a standard GitHub workflow for contributions:

1.  **Fork the Repository:** Create your own fork of the `AdGuard-FilterList-Manager-Python-Lib` repository.
2.  **Clone Locally:** Clone your forked repository to your development machine.
    ```bash
    git clone git@github.com:<your-username>/AdGuard-FilterList-Manager-Python-Lib.git
    cd AdGuard-FilterList-Manager-Python-Lib
    ```
3.  **Create a New Branch:** Start a new feature branch for your contribution. Use descriptive names following Conventional Commits.
    ```bash
    git checkout -b feat/your-feature-description
    # or
    git checkout -b fix/your-bug-fix-description
    ```
4.  **Make Your Changes:** Implement your feature or bug fix, adhering to the project's architectural principles and coding standards.
5.  **Test Your Changes:** Ensure all tests pass and new tests are added for any new functionality or bug fixes.
    ```bash
    # Install dependencies
    uv pip install -r requirements.txt
    uv pip install -r requirements-dev.txt

    # Run linters and formatters
    ruff check .
    ruff format .

    # Run tests
    pytest
    ```
6.  **Commit Your Changes:** Commit your changes using the Conventional Commits specification.
    ```bash
    git commit -m "feat: Add new filter list sorting algorithm"
    # or
    git commit -m "fix: Resolve issue with dynamic list updates"
    ```
7.  **Push to Your Fork:** Push your branch to your forked repository.
    ```bash
    git push origin feat/your-feature-description
    ```
8.  **Open a Pull Request:** Create a Pull Request (PR) from your branch to the `main` branch of the original `AdGuard-FilterList-Manager-Python-Lib` repository.

## 3. Development Environment Setup

To contribute, you'll need to set up your local development environment:

1.  **Install Python:** Ensure you have Python 3.10+ installed.
2.  **Install `uv`:** Install the `uv` package manager (recommended for speed and efficiency).
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
3.  **Clone Repository:** (As described above)
4.  **Install Dependencies:** Use `uv` to install project and development dependencies.
    ```bash
    cd AdGuard-FilterList-Manager-Python-Lib
    uv pip install -r requirements.txt
    uv pip install -r requirements-dev.txt
    ```

## 4. Coding Standards

All code must adhere to the Apex Technical Authority's coding standards:

*   **Language:** Python 3.10+
*   **Package Manager:** `uv`
*   **Linter & Formatter:** `Ruff` (configured via `pyproject.toml`)
*   **Testing Framework:** `Pytest`
*   **Architectural Principles:** SOLID, DRY, KISS, CQS, 12-Factor App.
*   **Code Style:** Strictly follow PEP 8, enforced by Ruff. Code must be self-documenting; avoid excessive comments.
*   **Testing:** Every source file must have a corresponding test file in the `tests/` directory. Aim for 100% test coverage for all implemented features.
*   **Security:** Sanitize all inputs. Follow OWASP Top 10 principles.
*   **Error Handling:** Fail fast. Implement robust error handling and recovery mechanisms.

## 5. Pull Request Guidelines

*   **Single Responsibility:** Each PR should ideally address a single feature, bug fix, or improvement.
*   **Clear Description:** Provide a concise summary of the changes, the problem addressed, and the solution implemented. Link to any relevant issues.
*   **Tests Included:** Ensure all new code is accompanied by comprehensive tests.
*   **CI/CD Passes:** Your PR must pass all automated checks in the CI/CD pipeline (linting, formatting, testing).
*   **Review:** Be prepared to engage with reviewers and make necessary adjustments.

## 6. Project Structure & Architecture

This project follows a modular structure optimized for maintainability and scalability. Key directories include:

*   `src/` (or `app/`): Contains the core application logic, structured into modules and features.
*   `tests/`: Houses all unit, integration, and end-to-end tests.
*   `scripts/`: Utility scripts for management, maintenance, and automation.
*   `docs/`: Project documentation (excluding README).

We aim for a **Modular Monolith** architecture, where components are well-defined and loosely coupled, allowing for potential future migration to microservices if required.

## 7. Reporting Issues

If you encounter a bug or have a feature request, please open an issue on GitHub. Use the provided templates (`bug_report.md`) and provide as much detail as possible, including:

*   A clear, concise description of the problem or feature.
*   Steps to reproduce the bug.
*   Expected behavior vs. Actual behavior.
*   Relevant environment details (Python version, OS, etc.).
*   Screenshots or error logs if applicable.

## 8. Feature Requests

For feature requests, please create an issue and describe the desired functionality. Explain the benefits and potential use cases. We will evaluate requests based on project goals and available resources.

## 9. Star ⭐ this Repo

If you find this project useful or are contributing, please consider starring the repository to show your support!
