# Security Policy

## Supported Versions

We are committed to the security of our users and strive to ensure that all supported versions of this project are free from critical vulnerabilities.

| Version | Supported          |
|---------|--------------------|
| 1.x     | :white_check_mark: |

*Note: Only the latest stable major version (1.x) is actively supported for security updates.*

## Reporting a Vulnerability

We take security vulnerabilities very seriously. If you discover a security issue, please report it responsibly to us, providing as much detail as possible.

**Disclosure Policy:** We ask that you not disclose any vulnerability information publicly until we have had the opportunity to fix it. We will not take legal action against researchers who act in good faith.

**Reporting Channel:**

Please report any security vulnerabilities via email to: `security@chirag127.dev`

**Information to Include:**

*   A clear and concise description of the vulnerability.
*   The affected version(s) of the software.
*   Steps to reproduce the vulnerability.
*   Proof-of-concept (PoC) code, if applicable.
*   Your suggested mitigation or fix, if you have one.

We will acknowledge your report promptly and aim to provide a response within **48 business hours**.

## Security Practices

This project adheres to the following security practices:

*   **Dependency Management:** We regularly audit and update project dependencies to mitigate known vulnerabilities, utilizing tools like `uv` and `Ruff`'s security checks.
*   **Code Review:** All code changes undergo rigorous review, with a focus on security best practices, including input validation, secure handling of sensitive data, and prevention of common attack vectors.
*   **Linters & Static Analysis:** We leverage `Ruff` for linting and static analysis to catch potential security flaws early in the development cycle.
*   **Testing:** Comprehensive unit and integration tests are in place, including tests for edge cases and security-related scenarios. Automated testing is performed on every commit via CI/CD pipelines.
*   **Principle of Least Privilege:** Components and processes operate with the minimum level of privilege necessary to perform their function.
*   **Secure Defaults:** The library is designed with secure configurations as the default.

Thank you for helping keep this project secure!
