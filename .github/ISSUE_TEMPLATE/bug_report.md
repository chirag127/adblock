---
name: Bug Report
about: Report a bug or unexpected behavior
title: "Bug: [Concise description of the issue]"
labels: bug, triage
assignees: ""

body:
  - type: markdown
    attributes:
      value: | # Use the following template to report a bug.
        Thank you for contributing to **AdGuard-FilterList-Manager-Python-Lib**!
        Please provide as much detail as possible to help us understand and fix the issue.

        **Apex Agent Directives:**
        - **Stack:** Python (uv, Ruff, Pytest)
        - **Architecture:** Modular Monolith / Microservices (or as appropriate)
        - **Testing:** Pytest (Unit Tests)
        - **Linting:** Ruff

        --- # END OF AGENT DIRECTIVES ---

  - type: markdown
    attributes:
      value: | # If you have a Stack Overflow or similar question, please ask it [here](ADD_FORUM_LINK_HERE).
        **BLUF:** Please describe the bug concisely.

  - type: input
    id: environment
    attributes:
      label: "Environment"
      description: "Which version of AdGuard-FilterList-Manager-Python-Lib are you using? What is your Python version? Any other relevant environment details?"
      placeholder: "e.g., Python 3.12.0, AdGuard-FilterList-Manager-Python-Lib v1.2.3"
    validations:
      required: true

  - type: textarea
    id: steps-to-reproduce
    attributes:
      label: "Steps to Reproduce"
      description: "Provide a clear and concise sequence of steps to reproduce the bug."
      placeholder: "1. Go to X
2. Click on Y
3. Observe Z"
    validations:
      required: true

  - type: textarea
    id: expected-behavior
    attributes:
      label: "Expected Behavior"
      description: "What did you expect to happen?"
      placeholder: "e.g., The list should be sorted alphabetically."
    validations:
      required: true

  - type: textarea
    id: actual-behavior
    attributes:
      label: "Actual Behavior"
      description: "What actually happened? Include any error messages or stack traces."
      placeholder: "e.g., The list remains unsorted, and an error is logged: ..."
    validations:
      required: true

  - type: textarea
    id: screenshots-logs
    attributes:
      label: "Screenshots / Logs (Optional)"
      description: "Add any relevant screenshots or logs that can help explain your problem."
      placeholder: "(Attach files here)"
    validations:
      required: false

  - type: textarea
    id: additional-context
    attributes:
      label: "Additional Context (Optional)"
      description: "Add any other context about the problem here. For example, specific filter lists affected, command-line arguments used, etc."
      placeholder: "e.g., This bug only occurs when processing AdGuard DNS filter lists."
    validations:
      required: false

---
