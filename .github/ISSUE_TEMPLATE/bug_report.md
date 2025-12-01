---
name: 🐛 Bug Report
about: Report a flaw, unexpected behavior, or deviation from specification.
title: "[BUG]: Concise summary of the issue (e.g., Filter list update fails on certain remote sources)"
labels: [ "bug", "triage/priority-medium" ]
assignees: ""

---

## 1. BLUF: Brief, Low-Fidelity Summary

Describe the bug in one clear sentence. What is happening that should not be happening?

> **Example:** The `list_sorter.py` script crashes with a KeyError when processing lists that contain comments starting with `! Title: `.

---

## 2. ENVIRONMENT & REPRODUCIBILITY

To ensure rapid diagnosis, detail the exact conditions under which the failure occurs. Follow the **F.I.R.S.T.** testing mandate.

### 2.1 System State

*   **Operating System:** (e.g., Ubuntu 24.04, Windows 11 Build 26002, macOS Sonoma)
*   **Python Version:** (e.g., `python --version`)
*   **uv/Ruff/Pytest Version:** (If applicable, check `uv list`)
*   **Execution Context:** (Local script execution, CI/CD pipeline run, Docker container)

### 2.2 Steps to Reproduce (STR)

Provide **atomic, precise, and repeatable** steps. Assume a fresh clone (`git clone`).

1.  Clone the repository:
    ```bash
    git clone [REPO_URL]
    cd AdGuard-FilterList-Manager-Python-Lib
    ```
2.  Ensure environment is set up (e.g., `uv venv && uv pip install -e .[dev]`)
3.  Execute the command that triggers the bug:
    ```bash
    # INSERT THE EXACT COMMAND HERE
    python src/management/process_lists.py --source=example_bad_source.txt
    ```
4.  Observe the failure.

---

## 3. EXPECTED VS. ACTUAL BEHAVIOR

### 🛑 Expected Result

What should the application have done according to the specification or design intent?

### 🚨 Actual Result

What did the application *actually* do? Include all relevant console output, stack traces, or error messages.

```text
# PASTE FULL STACK TRACE/OUTPUT HERE (DO NOT SUMMARIZE)

Traceback (most recent call last):
  File "...", line X, in <module>
    ... 
KeyError: 'Title'
```

---

## 4. ARCHITECTURAL DEVIATION & CONTEXT

Which component or architectural principle (SOLID, DRY) appears to be violated by this bug?

*   **Suspected Module/Function:** (e.g., `utils.file_handling`, `cli_parser`)
*   **Potential Violation:** (e.g., Violates SRP because the function is parsing AND filtering.)

---

## 🤖 AGENT DIRECTIVES FOR REPAIR

If an autonomous agent is assigned this ticket, they must adhere to the following **Apex Protocol**:

<details>
<summary>Click to view Apex Technical Authority Mandates</summary>

**Tech Stack:** Python 3.12+, uv, Ruff, Pytest.

**Repair Mandates:**
1.  **GUARD CLAUSE:** Implement immediate input validation (Fail Fast) at the boundary of the failing function.
2.  **TEST FIRST:** Create a regression test in `tests/unit/` that replicates this exact failure state before any code is modified.
3.  **LINTING:** Ensure the fix adheres strictly to **Ruff** standards and Python PEP 8/PEP 8201 compliance.
4.  **REFACTORING:** If the issue stems from complex state mutation, apply the **Command/Query Separation (CQS)** principle.

</details>