# 🛡️ Security Policy for AdGuard-FilterList-Manager-Python-Lib

As an Apex-Architected project, security is treated as a primary non-functional requirement, adhering strictly to the **Zero Trust Model** and **OWASP Top 10 (2025)** recommendations. We prioritize the integrity and privacy afforded by the managed filter lists.

## Supported Versions

Only the latest stable release (following Semantic Versioning) and the immediate preceding minor release are actively maintained for security patches. Older versions are considered end-of-life and will not receive updates.

| Version | Status | Patch Commitment |
| :--- | :--- | :--- |
| `vX.Y.Z` (Latest) | Active | Immediate |
| `vX.(Y-1).Z` | Maintained | 7 Days |

## 🚨 Reporting a Vulnerability

We take security reports extremely seriously. To protect both the project maintainers and our users, **DO NOT** report security vulnerabilities publicly via GitHub Issues or Pull Requests.

**Responsible Disclosure Protocol:**

1.  **Private Communication:** Immediately email the security team at: `security@apex-architect.dev` (Placeholder for domain owner).
2.  **Provide Detail:** Include the repository name, affected version(s), a detailed proof-of-concept (PoC) if possible, and any mitigation steps you have identified.
3.  **Encryption:** Sensitive data (e.g., credentials, full PoCs) should be encrypted using a PGP key if available.

We will acknowledge receipt of your report within **48 hours**.

## Disclosure Timeline

Our goal is rapid remediation. We adhere to the following timeline upon receiving a valid vulnerability report:

*   **Initial Triage:** 24 hours.
*   **Patch Development:** Up to 60 days, depending on complexity.
*   **Public Disclosure:** We aim to release the patch and disclose details **no later than 90 days** after initial report, unless otherwise agreed upon with the reporter.

## Automated Security Auditing (DevSecOps)

This repository enforces security checks within its CI/CD pipeline (`.github/workflows/ci.yml`). These automated gates ensure supply chain security:

1.  **Dependency Scanning:** All packages managed by `uv` are scanned for known CVEs on every push to the main branch.
2.  **SBOM Generation:** A Software Bill of Materials (SBOM) is generated and attached to production releases to ensure full transparency of project dependencies.
3.  **Static Analysis (Ruff):** Aggressive linting profiles are applied to catch security pitfalls, misconfigurations, and common Python anti-patterns (`fail-fast` philosophy).

## Input Validation & Sanitization

Given that this library manages configuration data (filter lists), all inputs processed by management scripts must be treated as **hostile**. Specific attention is paid to:

*   **Path Traversal:** Preventing scripts from reading/writing outside intended configuration directories.
*   **Injection Attacks:** Strict validation and escaping when constructing system commands or configuration files for AdGuard clients.
*   **Resource Exhaustion:** Logic controlling list merging or sorting must implement safeguards against infinite loops or excessive memory allocation when handling massive, poorly formed external lists.

---

*This repository is maintained by the Apex Technical Authority team. We thank you for your diligence in helping keep this infrastructure secure.*