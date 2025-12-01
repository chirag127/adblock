<div align="center">

  <img src="https://raw.githubusercontent.com/chirag127/AdGuard-FilterList-Management-Python-Lib/main/.github/assets/banner.png" alt="AdGuard FilterList Management Python Lib Banner"/>

  <h1>AdGuard FilterList Management Python Lib</h1>

  <p>A high-performance Python library for creating, managing, and optimizing AdGuard filter lists. Automates rule generation, deduplication, and sorting to enhance ad and tracker blocking across all platforms.</p>

  <!-- Badges -->
  <div>
    <a href="https://github.com/chirag127/AdGuard-FilterList-Management-Python-Lib/actions/workflows/ci.yml">
      <img src="https://img.shields.io/github/actions/workflow/status/chirag127/AdGuard-FilterList-Management-Python-Lib/ci.yml?style=flat-square&logo=github&label=Build" alt="Build Status"/>
    </a>
    <a href="https://codecov.io/gh/chirag127/AdGuard-FilterList-Management-Python-Lib">
      <img src="https://img.shields.io/codecov/c/github/chirag127/AdGuard-FilterList-Management-Python-Lib?style=flat-square&logo=codecov&label=Coverage" alt="Code Coverage"/>
    </a>
    <a href="#">
      <img src="https://img.shields.io/badge/Python-3.12%2B-blue?style=flat-square&logo=python" alt="Python Version"/>
    </a>
    <a href="#">
      <img src="https://img.shields.io/badge/Linter-Ruff-blueviolet?style=flat-square&logo=ruff" alt="Linter: Ruff"/>
    </a>
    <a href="https://github.com/chirag127/AdGuard-FilterList-Management-Python-Lib/blob/main/LICENSE">
      <img src="https://img.shields.io/github/license/chirag127/AdGuard-FilterList-Management-Python-Lib?style=flat-square&label=License" alt="License"/>
    </a>
    <a href="https://github.com/chirag127/AdGuard-FilterList-Management-Python-Lib/stargazers">
      <img src="https://img.shields.io/github/stars/chirag127/AdGuard-FilterList-Management-Python-Lib?style=flat-square&logo=github&label=Stars" alt="GitHub Stars"/>
    </a>
  </div>

  <br/>

  <a href="https://github.com/chirag127/AdGuard-FilterList-Management-Python-Lib/stargazers"><strong>Star ⭐ this Repo</strong></a> to support its development!

</div>

---

## Table of Contents

- [✨ Core Features](#-core-features)
- [🏗️ Architecture Overview](#️-architecture-overview)
- [🤖 AI Agent Directives](#-ai-agent-directives)
- [🚀 Getting Started](#-getting-started)
- [💡 Usage Example](#-usage-example)
- [🛠️ Development](#️-development)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## ✨ Core Features

- **High-Performance Parsing:** Ingests massive filter lists with minimal memory overhead.
- **Intelligent Deduplication:** Removes redundant rules, including cosmetic and network-level duplicates.
- **Optimized Sorting:** Arranges rules for faster processing by AdGuard engines.
- **Automated Rule Generation:** Programmatically create complex filtering rules from source data.
- **Extensible Rule System:** Easily define and integrate custom rule types.
- **CI/CD Ready:** Built for integration into automated list generation and deployment pipelines.

---

## 🏗️ Architecture Overview

This library follows a **Modular Monolith** pattern, ensuring high cohesion and low coupling between components. This design enhances maintainability and simplifies testing.

sh
.
├── src/
│   └── adguard_filter_lib/    # Main library source code
│       ├── __init__.py
│       ├── core/                # Core logic for processing lists
│       │   ├── parser.py        # Rule parsing engine
│       │   ├── generator.py     # Rule generation engine
│       │   └── optimizer.py     # Deduplication and sorting logic
│       ├── rules/               # Rule object definitions
│       │   ├── base_rule.py
│       │   └── rule_types.py
│       └── utils/               # Helper utilities
│           └── file_handler.py
├── tests/                     # Unit and integration tests
│   ├── test_parser.py
│   └── test_optimizer.py
├── scripts/                   # Example automation scripts
│   └── build_list.py
├── pyproject.toml             # Project configuration (uv, Ruff)
└── README.md


---

## 🤖 AI Agent Directives

<details>
<summary><strong>Click to expand: Directives for AI Agents & Future Development</strong></summary>

<br/>

# SYSTEM: APEX TECHNICAL AUTHORITY & ELITE ARCHITECT (DECEMBER 2025 EDITION)

## 1. IDENTITY & PRIME DIRECTIVE
**Role:** You are a Senior Principal Software Architect and Master Technical Copywriter with **40+ years of elite industry experience**. You operate with absolute precision, enforcing FAANG-level standards and the wisdom of "Managing the Unmanageable."
**Context:** Current Date is **December 2025**. You are building for the 2026 standard.
**Output Standard:** Deliver **EXECUTION-ONLY** results. No plans, no "reporting"—only executed code, updated docs, and applied fixes.
**Philosophy:** "Zero-Defect, High-Velocity, Future-Proof."

---

## 2. INPUT PROCESSING & COGNITION
* **SPEECH-TO-TEXT INTERPRETATION PROTOCOL:**
    * **Context:** User inputs may contain phonetic errors (homophones, typos).
    * **Semantic Correction:** **STRICTLY FORBIDDEN** from executing literal typos. You must **INFER** technical intent based on the project context.
    * **Logic Anchor:** Treat the `README.md` as the **Single Source of Truth (SSOT)**.
* **MANDATORY MCP INSTRUMENTATION:**
    * **No Guessing:** Do not hallucinate APIs.
    * **Research First:** Use `linkup`/`brave` to search for **December 2025 Industry Standards**, **Security Threats**, and **2026 UI Trends**.
    * **Validation:** Use `docfork` to verify *every* external API signature.
    * **Reasoning:** Engage `clear-thought-two` to architect complex flows *before* writing code.

---

## 3. CONTEXT-AWARE APEX TECH STACKS (LATE 2025 STANDARDS)
**Directive:** This repository adheres to the **Apex Python Standard** for high-performance libraries and automation tools.
* **Project Type:** Python Library (Data / Scripts / AI)
* **Stack:**
    * **Package & Environment Manager:** `uv` (The high-performance industry standard for 2026).
    * **Linter & Formatter:** `Ruff` (All-in-one, extreme performance).
    * **Testing Framework:** `Pytest` (For robust, scalable testing).
* **Architecture:** Adheres to a **Modular Monolith** pattern. Core functionalities are encapsulated in distinct, loosely-coupled modules (`core/`, `utils/`, `rules/`) to ensure high cohesion and maintainability.
* **Verification Commands:**
    * **Install Dependencies:** `uv pip install -r requirements.txt`
    * **Run Linter:** `uv run ruff check .`
    * **Run Formatter:** `uv run ruff format .`
    * **Run Tests:** `uv run pytest`

---

## 4. AI ORCHESTRATION & GEMINI PROTOCOL (DECEMBER 2025)
**Mandate:** If integrating AI, strictly follow this **Fallback Cascade** for the Google Gemini API.
* **Tier 1 (Intelligence):** `gemini-3-pro` (Stable Dec 2025) - Multimodal Reasoning.
* **Tier 2 (Reasoning):** `gemini-2.5-pro` (Legacy Stable) - Deep analysis/STEM.
* **Tier 3 (Balanced):** `gemini-2.5-flash` - High Volume/Low Latency.
* **Tier 4 (Speed):** `gemini-2.5-flash-lite` - Cost-efficiency.
* **Circuit Breaker:** If a model fails (429/500), trigger **Cool-Off** and fallback immediately.
* **Local AI Emulation:** Utilize Mock AI services during local development and CI runs to ensure predictable test outcomes and reduce API costs.

</details>

---

## 🚀 Getting Started

### Prerequisites

- Python 3.12+
- `uv` (Python package installer and virtual environment manager)

### Installation

1.  **Clone the repository:**
    bash
    git clone https://github.com/chirag127/AdGuard-FilterList-Management-Python-Lib.git
    cd AdGuard-FilterList-Management-Python-Lib
    

2.  **Create and activate a virtual environment:**
    bash
    uv venv
    source .venv/bin/activate
    

3.  **Install dependencies:**
    bash
    uv pip install -r requirements.txt
    

---

## 💡 Usage Example

Here is a basic example of how to read a filter list, optimize it, and write the result to a new file.

python
from adguard_filter_lib.core.optimizer import optimize_list
from adguard_filter_lib.utils.file_handler import read_rules, write_rules

def main():
    # Path to your source and destination files
    input_file = 'path/to/your/source-list.txt'
    output_file = 'path/to/your/optimized-list.txt'

    print(f"Reading rules from {input_file}...")
    rules = read_rules(input_file)
    initial_count = len(rules)
    print(f"Read {initial_count} rules.")

    print("Optimizing list (deduplicating and sorting)...")
    optimized_rules = optimize_list(rules)
    final_count = len(optimized_rules)
    print(f"Optimization complete. Final rule count: {final_count}.")

    print(f"Writing optimized rules to {output_file}...")
    write_rules(optimized_rules, output_file)
    print("Done!")

if __name__ == "__main__":
    main()


---

## 🛠️ Development

This project uses `uv` for environment management and `Ruff` for linting and formatting to ensure code quality and consistency.

### Scripts

| Command            | Description                                        |
| ------------------ | -------------------------------------------------- |
| `uv run lint`      | Lints the codebase using Ruff.                     |
| `uv run format`    | Formats the codebase using Ruff.                   |
| `uv run test`      | Runs the entire test suite using Pytest.           |
| `uv run test:cov`  | Runs tests and generates a coverage report.        |

### Core Principles

- **SOLID:** Code is structured to be understandable, flexible, and maintainable.
- **DRY (Don't Repeat Yourself):** Reusable components are abstracted to avoid code duplication.
- **YAGNI (You Ain't Gonna Need It):** Features are added only when necessary to avoid over-engineering.

---

## 🤝 Contributing

Contributions are welcome! Please read the [**CONTRIBUTING.md**](.github/CONTRIBUTING.md) file for guidelines on how to submit pull requests, report issues, and suggest enhancements.

---

## 📄 License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License**. See the [**LICENSE**](LICENSE) file for details.
