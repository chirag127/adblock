# AdGuard FilterList Management Python Library

<p align="center">
  <a href="https://github.com/chirag127/AdGuard-FilterList-Management-Python-Lib/actions/workflows/ci.yml">
    <img src="https://github.com/chirag127/AdGuard-FilterList-Management-Python-Lib/actions/workflows/ci.yml/badge.svg?style=flat-square" alt="CI/CD Pipeline">
  </a>
  <a href="https://codecov.io/gh/chirag127/AdGuard-FilterList-Management-Python-Lib">
    <img src="https://img.shields.io/codecov/c/github/chirag127/AdGuard-FilterList-Management-Python-Lib?style=flat-square&token=CODECOV_TOKEN_PLACEHOLDER" alt="Code Coverage">
  </a>
  <a href="https://github.com/astral-sh/uv">
    <img src="https://img.shields.io/badge/tech-Python%20%7C%20Ruff%20%7C%20uv-blue?style=flat-square" alt="Tech Stack">
  </a>
  <a href="https://github.com/astral-sh/ruff">
    <img src="https://img.shields.io/badge/linter-Ruff-blueviolet?style=flat-square" alt="Linter">
  </a>
  <a href="./LICENSE">
    <img src="https://img.shields.io/github/license/chirag127/AdGuard-FilterList-Management-Python-Lib?style=flat-square" alt="License">
  </a>
  <a href="https://github.com/chirag127/AdGuard-FilterList-Management-Python-Lib/stargazers">
    <img src="https://img.shields.io/github/stars/chirag127/AdGuard-FilterList-Management-Python-Lib?style=flat-square&logo=github" alt="GitHub Stars">
  </a>
</p>

<p align="center">
  <em>A high-performance Python library for creating, managing, and optimizing AdGuard filter lists. It automates rule generation, deduplication, and sorting to enhance ad and tracker blocking across all platforms, boosting privacy and security.</em>
</p>

<p align="center">
  <a href="https://github.com/chirag127/AdGuard-FilterList-Management-Python-Lib/stargazers">
    <img src="https://img.shields.io/badge/-Star%20%E2%AD%90%20this%20Repo-gray?style=for-the-badge&logo=github" alt="Star this Repo">
  </a>
</p>

---

## Table of Contents

- [✨ Features](#-features)
- [🏗️ Architecture](#️-architecture)
- [🚀 Quick Start](#-quick-start)
- [🛠️ Development Setup](#️-development-setup)
- [🤖 AI Agent Directives](#-ai-agent-directives)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

---

## ✨ Features

- **Automated Rule Processing:** Ingests multiple filter list sources (local or remote).
- **High-Performance Deduplication:** Efficiently removes duplicate rules to minimize list size.
- **Optimized Sorting:** Sorts rules for faster processing by AdGuard clients.
- **Comment & Metadata Preservation:** Retains important comments and metadata from source files.
- **Extensible Design:** Easily add custom processing or filtering steps.
- **Scalable:** Built to handle millions of rules from dozens of sources without performance degradation.

## 🏗️ Architecture

This project follows a clean, modular architecture, adhering to SOLID principles and strict separation of concerns. All source code is contained within the `src/` directory, and all tests are isolated in the `tests/` directory.

sh
.AdGuard-FilterList-Management-Python-Lib/
├── .github/                  # GitHub Actions workflows & templates
│   ├── workflows/ci.yml      # CI/CD pipeline
│   └── ...
├── src/
│   └── adguard_filter_lib/   # Main library source code
│       ├── __init__.py
│       ├── manager.py          # Core FilterListManager class
│       └── utils.py            # Helper functions
├── tests/
│   ├── unit/                 # Unit tests for isolated components
│   └── integration/          # Integration tests for component interaction
├── .gitignore
├── LICENSE
├── pyproject.toml            # Project metadata and dependencies (uv/ruff)
└── README.md


## 🚀 Quick Start

Get started by installing the library and running a basic optimization task.

1.  **Installation (Requires Python 3.10+)**

    bash
    # Coming soon to PyPI
    pip install adguard-filter-lib
    

2.  **Example Usage**

    python
    from adguard_filter_lib import FilterListManager

    # Define a list of source URLs
    source_urls = [
        "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_2_Base/filter.txt",
        "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_1_English/filter.txt"
    ]

    # Initialize the manager
    manager = FilterListManager(sources=source_urls)

    # Process and optimize the lists
    print("Loading and parsing sources...")
    manager.load_sources()
    print(f"Initial rule count: {manager.rule_count}")

    print("Deduplicating rules...")
    manager.deduplicate()
    print(f"Rule count after deduplication: {manager.rule_count}")

    print("Sorting rules...")
    manager.sort()

    # Save the final, optimized list to a file
    output_file = "optimized-adguard-list.txt"
    manager.save_to_file(output_file)

    print(f"\n✅ Optimized list created at '{output_file}' with {manager.rule_count} unique rules.")
    

## 🛠️ Development Setup

To contribute to this project, follow these steps to set up your local development environment.

1.  **Clone the Repository**

    bash
    git clone https://github.com/chirag127/AdGuard-FilterList-Management-Python-Lib.git
    cd AdGuard-FilterList-Management-Python-Lib
    

2.  **Set up Virtual Environment & Install Dependencies using `uv`**

    bash
    # Create a virtual environment
    uv venv

    # Activate the environment
    # On macOS/Linux
    source .venv/bin/activate
    # On Windows
    .venv\Scripts\activate

    # Install dependencies from pyproject.toml
    uv pip install -e .[dev]
    

3.  **Run Quality Checks & Tests**

    bash
    # Format code with Ruff
    ruff format .

    # Lint code with Ruff
    ruff check .

    # Run tests with Pytest
    pytest
    

## 🤖 AI Agent Directives

<details>
<summary><strong>SYSTEM: APEX TECHNICAL AUTHORITY (DECEMBER 2025) - Agent Operating Instructions</strong></summary>

### 1. IDENTITY & PRIME DIRECTIVE
**Role:** You are a Senior Principal Software Architect operating under the **Apex Technical Authority** protocol. Your function is to enhance and maintain this Python library to FAANG-level standards for 2026 and beyond.
**Philosophy:** "Zero-Defect, High-Velocity, Future-Proof."

### 2. CONTEXT-AWARE APEX TECH STACKS (LATE 2025 STANDARDS)
This project is classified as **SCENARIO C: DATA / SCRIPTS / AI (Python)**. You **MUST** adhere to this toolchain:
- **Package/Environment Manager:** `uv` is the mandatory standard for speed and dependency resolution.
- **Linter/Formatter:** `Ruff` is the exclusive tool for all linting and formatting. No other linters are permitted.
- **Testing Framework:** `Pytest` is the sole framework for all unit, integration, and end-to-end tests.
- **Architecture:** Maintain a Modular Monolith structure. Ensure new features are encapsulated and have clear interfaces.

### 3. RECURSIVE PERFECTION LOOP (THE "ZERO-ERROR" MANDATE)
You must execute the following loop until the build is perfectly clean before committing:
1.  **Analyze:** Scan the codebase for architectural deviations.
2.  **Fix:** Apply fixes based on SOLID principles.
3.  **Lint/Format:** Run `ruff format . && ruff check --fix .`.
4.  **Test:** Run `pytest`.
5.  **Decision Gate:** If errors/warnings exist, return to step 2. If clean, proceed to commit.

### 4. CORE ARCHITECTURAL PRINCIPLES
- **SOLID MANDATE:** Enforce Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion principles rigourously.
- **ROOT DIRECTORY HYGIENE:** The root is for configuration only (`pyproject.toml`, `README.md`). All Python source code resides in `src/`. All tests reside in `tests/`.
- **CQS (Command-Query Separation):** Methods must either return a value (Query) or mutate state (Command), but not both.

### 5. COMPREHENSIVE TESTING & VERIFICATION STRATEGY
- **FOLDER SEPARATION PROTOCOL (STRICT):** The `src/` directory is a **Production-Only Zone**. It must contain **ZERO** test files. **ALL** verification code (unit tests, integration tests) must reside exclusively in `tests/`.
- **COVERAGE MANDATE:** Strive for 90%+ branch coverage. All new code **MUST** be accompanied by tests.
- **TESTING PYRAMID (F.I.R.S.T.):** Tests must be Fast, Isolated, and Repeatable.

### 6. DOCUMENTATION & VERSION CONTROL
- **HERO-TIER README:** The README must be updated **IN THE SAME TURN** as any code changes affecting public APIs or setup steps.
- **CONVENTIONAL COMMITS:** All commit messages **MUST** follow the Conventional Commits specification (e.g., `feat:`, `fix:`, `docs:`, `test:`).

### 7. AUTOMATION SINGULARITY (GITHUB ACTIONS)
All CI workflows must perform these checks. A Pull Request cannot be merged if any step fails.
1.  **Integrity:** `ruff check .`
2.  **Testing:** `pytest`
3.  **Security:** `pip-audit`

</details>

## 🤝 Contributing

Contributions are welcome! Please read the [Contributing Guidelines](./.github/CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📜 License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License** - see the [LICENSE](./LICENSE) file for details.
