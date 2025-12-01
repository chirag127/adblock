# 🚀 Pull Request Template: Apex Integrity Check

**Branch:** `{{_target_branch}}` <- `{{head_ref}}`

## 1. Blurb: The 10-Second Summary (BLUF)

*Concise description of what this PR does, why it was necessary, and its core impact.* (e.g., `fix: Resolves issue #42 by implementing exponential backoff for external API calls.`) 

---

## 2. Type of Change (Select one or more)

- [ ] `breaking`: API change or major refactor that requires consumer updates.
- [ ] `feat`: A new feature or capability.
- [ ] `fix`: A bug fix (non-breaking).
- [ ] `docs`: Documentation only changes.
- [ ] `style`: Formatting, missing semicolons, code style fixes (managed by Biome/Ruff).
- [ ] `refactor`: Code cleanup/restructuring without changing functionality.
- [ ] `perf`: A code change that improves performance.
- [ ] `test`: Adding missing tests or correcting existing tests.
- [ ] `chore`: Maintenance tasks, build process, or dependency updates.

---

## 3. Architectural Verification Checklist (Mandatory)

*Ensure this PR adheres to the **Apex Architectural Directives** defined in `AGENTS.md`.*

- [ ] **SOLID Adherence:** Does this change respect SRP/OCP/etc.?
- [ ] **CQS Enforced:** Are commands strictly modifying state and queries strictly retrieving data?
- [ ] **Fail Fast:** Are inputs validated immediately? Are critical I/O wrapped in resilient error handlers?
- [ ] **DRY Principle:** Have I avoided unnecessary code duplication?
- [ ] **Testing Coverage:** Have I added/updated tests to cover all new/changed logic paths?
- [ ] **Performance Intent:** If this is a performance change, is the complexity improved ($O(n)$ vs $O(n^2)$)?
- [ ] **Security Scan:** Have I sanitized all external inputs (if applicable)?

---

## 4. Technical Details & Rationale

### A. The Why (Context)
<!-- Explain the motivation behind this change. Reference the corresponding Issue/Ticket if available. -->

### B. The How (Implementation Summary)
<!-- Briefly describe the main classes, functions, or components modified and the pattern used (e.g., 'Implemented the Strategy Pattern for filter aggregation'). -->

### C. Code Snippets (If necessary)

```python
# Example of a critical change that needs review
# Add the relevant code snippet here.
```

---

## 5. Pre-Merge Verification Checklist (Local Execution)

*Self-verification steps before requesting review.*

- [ ] **Linter Check:** `ruff check --fix .` passed with zero errors.
- [ ] **Test Suite:** `pytest` executed successfully against the entire suite.
- [ ] **Documentation Sync:** `README.md` and relevant docstrings updated for new features.
- [ ] **Dependency Review:** No new major dependencies added without explicit security review.

---

## 6. Screenshots / Artifacts (If UI/Output Affected)

<!-- Attach screenshots or relevant execution output if this change impacts command line output or generated files. -->

**Reviewer Note:** Please focus review on sections [X] and [Y]. See commit `[HASH]` for the core logic change.