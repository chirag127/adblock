# Security Policy

## Supported Versions

We actively support and patch the latest stable version of **AdGuard-FilterList-Manager-Python-Lib**. Older versions are not actively maintained and may contain unaddressed vulnerabilities.

## Reporting a Vulnerability

We take security seriously. If you discover any security vulnerabilities, please report them responsibly. We will investigate and address all valid reports promptly.

**DO NOT** open a public issue for security vulnerabilities. Instead, please:

1.  **Email:** Send a detailed report to `security@example.com` (replace with actual security contact email).
2.  **Subject Line:** Use the subject: `SECURITY Vulnerability Report - AdGuard-FilterList-Manager-Python-Lib`.
3.  **Content:** Include the following in your report:
    *   A clear description of the vulnerability.
    *   Affected version(s) of the library.
    *   Steps to reproduce the vulnerability.
    *   Any recommended mitigation or fix.
    *   (Optional) Proof-of-concept code.

We will acknowledge receipt of your report within **48 hours** and will provide an estimated timeline for resolution. We will also work with you to coordinate a public disclosure once a fix is available and deployed.

## Vulnerability Disclosure Policy

*   **Confidentiality:** All security reports will be handled with strict confidentiality.
*   **No Harm:** Please do not exploit vulnerabilities in any way that could disrupt our services or impact users. Testing should be limited to identifying the vulnerability.
*   **Acknowledgement:** We will publicly acknowledge responsible disclosure efforts by security researchers (if they agree).

## Security Best Practices

As a library focused on managing filter lists, please adhere to the following when contributing or using this project:

*   **Input Validation:** Always validate and sanitize any external input used within scripts or configurations to prevent injection attacks.
*   **Dependency Management:** Ensure all dependencies are kept up-to-date and are sourced from trusted repositories. Regularly audit dependencies for known vulnerabilities.
*   **Code Review:** All code changes, especially those affecting security-sensitive areas, must undergo rigorous peer review.
*   **Principle of Least Privilege:** Scripts and operations should run with the minimum necessary permissions.

Thank you for helping us keep **AdGuard-FilterList-Manager-Python-Lib** secure.
