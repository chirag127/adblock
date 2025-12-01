# AdGuard FilterList Management Python Library

<div align="center">
  <img src="https://raw.githubusercontent.com/chirag127/AdGuard-FilterList-Management-Python-Lib/main/.github/assets/banner.png" alt="Project Banner">

  <p align="center">
    A high-performance Python library for creating, managing, and optimizing AdGuard filter lists.
    <br />
    Automates rule generation, deduplication, and sorting to enhance ad and tracker blocking across all platforms.
  </p>

  <p align="center">
    <!-- Badges -->
    <a href="https://github.com/chirag127/AdGuard-FilterList-Management-Python-Lib/actions/workflows/ci.yml">
      <img src="https://img.shields.io/github/actions/workflow/status/chirag127/AdGuard-FilterList-Management-Python-Lib/ci.yml?branch=main&style=flat-square&logo=githubactions&logoColor=white" alt="Build Status">
    </a>
    <a href="https://codecov.io/gh/chirag127/AdGuard-FilterList-Management-Python-Lib">
      <img src="https://img.shields.io/codecov/c/github/chirag127/AdGuard-FilterList-Management-Python-Lib?style=flat-square&logo=codecov&logoColor=white" alt="Code Coverage">
    </a>
    <a href="https://github.com/chirag127/AdGuard-FilterList-Management-Python-Lib">
      <img src="https://img.shields.io/badge/Python-3.12+-blue?style=flat-square&logo=python&logoColor=white" alt="Python Version">
    </a>
    <a href="https://github.com/astral-sh/ruff">
        <img src="https://img.shields.io/badge/Linter-Ruff-blueviolet?style=flat-square&logo=ruff" alt="Linter: Ruff">
    </a>
    <a href="https://github.com/chirag127/AdGuard-FilterList-Management-Python-Lib/blob/main/LICENSE">
      <img src="https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey.svg?style=flat-square" alt="License">
    </a>
    <a href="https://github.com/chirag127/AdGuard-FilterList-Management-Python-Lib/stargazers">
      <img src="https://img.shields.io/github/stars/chirag127/AdGuard-FilterList-Management-Python-Lib?style=flat-square&logo=github&logoColor=white" alt="GitHub stars">
    </a>
  </p>
  
  **Found this project useful? Star ⭐ it to show your support!**
</div>

---

## 🚀 Overview

`AdGuard-FilterList-Management-Python-Lib` provides a robust, developer-friendly toolkit for programmatic control over ad-blocking filter lists. It's engineered to handle large-scale rule sets with exceptional performance, automating the tedious tasks of syntax validation, deduplication, sorting, and optimization. This library is the perfect backend engine for custom ad-blocking solutions, research tools, or DevOps pipelines that manage network-wide privacy.

## ✨ Key Features

- **High-Performance Parsing:** Efficiently process tens of thousands of rules in seconds.
- **Automated Optimization:** Automatically sorts, deduplicates, and compresses filter lists for optimal performance in AdGuard clients.
- **Rule Validation:** Built-in syntax checking to prevent invalid or broken rules from being deployed.
- **Extensible API:** A clean, modular API for creating, reading, updating, and deleting rules.
- **Source Aggregation:** Easily combine multiple source lists into a single, optimized output file.
- **Type-Hinted & Tested:** Fully type-hinted codebase with comprehensive unit tests for maximum reliability.

## 🏛️ Architecture

The library follows a modular design, separating core logic from file I/O and utility functions. This ensures maintainability and testability, allowing developers to easily extend or replace components.

sh
.AdGuard-FilterList-Management-Python-Lib/
├── src/adguard_filterlist_lib/
│   ├── __init__.py
│   ├── core.py         # Core list management and optimization logic
│   ├── parser.py       # Rule parsing and validation engine
│   ├── models.py       # Pydantic models for rule types
│   └── utils.py        # Helper functions
├── tests/
│   ├── test_core.py
│   └── test_parser.py
├── examples/
│   └── create_master_list.py
├── pyproject.toml      # Project metadata and dependencies (uv/Ruff)
├── README.md
└── LICENSE


## 📖 Table of Contents

1.  [Overview](#-overview)
2.  [Key Features](#-key-features)
3.  [Architecture](#️-architecture)
4.  [Installation & Setup](#-installation--setup)
5.  [Usage](#-usage)
6.  [Development](#-development)
7.  [Contributing](#-contributing)
8.  [License](#-license)
9.  [AI Agent Directives](#-ai-agent-directives)

## 🔧 Installation & Setup

This project uses `uv` for high-speed dependency management.

1.  **Clone the repository:**
    bash
    git clone https://github.com/chirag127/AdGuard-FilterList-Management-Python-Lib.git
    cd AdGuard-FilterList-Management-Python-Lib
    

2.  **Create and activate a virtual environment:**
    bash
    # Install uv if you haven't already
    # pip install uv

    uv venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    

3.  **Install dependencies:**
    bash
    uv pip install -r requirements.txt
    

## 💡 Usage

Here's a quick example of how to combine and optimize two filter lists.

python
# examples/create_master_list.py
from adguard_filterlist_lib.core import FilterListManager

# Define source files
list_a_path = 'source_lists/privacy_list.txt'
list_b_path = 'source_lists/annoyances_list.txt'

# Create a manager instance
manager = FilterListManager()

# Load rules from multiple sources
manager.load_from_file(list_a_path)
manager.load_from_file(list_b_path)

# Optimize the combined list (deduplicate, sort)
manager.optimize()

# Save the optimized master list
output_path = 'dist/master_filter_list.txt'
manager.save_to_file(output_path)

print(f"Successfully created optimized list at {output_path} with {manager.rule_count()} rules.")


## 🛠️ Development

This project adheres to modern Python development standards, utilizing `uv` and `Ruff` for a streamlined workflow.

| Command             | Description                                                   |
| ------------------- | ------------------------------------------------------------- |
| `uv pip install -r requirements-dev.txt` | Installs development dependencies.                            |
| `pytest`            | Runs the entire test suite.                                   |
| `ruff check .`      | Lints the codebase for errors and style issues.               |
| `ruff format .`     | Automatically formats the code according to project standards.|

### Core Principles

-   **SOLID:** Code is structured to be flexible, maintainable, and scalable.
-   **DRY (Don't Repeat Yourself):** Reusable logic is abstracted into utilities to avoid redundancy.
-   **YAGNI (You Ain't Gonna Need It):** We avoid over-engineering by focusing on delivering essential, high-value features.

## 🤝 Contributing

Contributions are welcome! Please see our [Contributing Guidelines](.github/CONTRIBUTING.md) for details on bug reports, feature requests, and pull requests. We follow a strict code of conduct and expect all contributors to do the same.

## 📜 License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License** - see the [LICENSE](LICENSE) file for details.

---

## 🤖 AI Agent Directives

<details>
<summary>Expand for AI Development Protocol (2026 Standard)</summary>

### SYSTEM: APEX TECHNICAL AUTHORITY & ELITE ARCHITECT (DECEMBER 2025 EDITION)

#### 1. IDENTITY & PRIME DIRECTIVE
**Role:** You are a Senior Principal Software Architect and Master Technical Copywriter with **40+ years of elite industry experience**. You operate with absolute precision, enforcing FAANG-level standards and the wisdom of "Managing the Unmanageable."
**Context:** Current Date is **December 2025**. You are building for the 2026 standard.
**Output Standard:** Deliver **EXECUTION-ONLY** results. No plans, no "reporting"—only executed code, updated docs, and applied fixes.
**Philosophy:** "Zero-Defect, High-Velocity, Future-Proof."

#### 2. CONTEXT-AWARE APEX TECH STACKS (LATE 2025 STANDARDS)
**Directives:** This project is identified as a Python library (`pyproject.toml`). The **Apex Python Toolchain** must be enforced.

-   **Stack:**
    -   **Package Manager:** `uv` is the exclusive tool for all dependency management and virtual environment operations. Do not use `pip` or `poetry` directly.
    -   **Linter/Formatter:** `Ruff` is the Single Source of Truth for code style, linting, and formatting. All commits must pass `ruff check .` and `ruff format .`.
    -   **Testing:** `Pytest` is the required framework for all unit, integration, and functional tests.

-   **Architecture:**
    -   **Modular Monolith:** Adhere to a modular structure within the `src` directory. Each module must have a clear responsibility (e.g., `parser`, `core`, `utils`).
    -   **Strict Typing:** All new code **MUST** be fully type-hinted using Python 3.12+ syntax.

#### 3. VERIFICATION & DEPLOYMENT PROTOCOL
**Mandate:** Before any pull request is merged, the following commands **MUST** execute successfully in the CI pipeline (`.github/workflows/ci.yml`).

1.  **Dependency Sync:** `uv pip sync requirements.txt`
2.  **Lint Check:** `ruff check .`
3.  **Format Check:** `ruff format --check .`
4.  **Unit Tests:** `pytest --cov=src`

Failure in any step is a hard block. No exceptions.

</details>
