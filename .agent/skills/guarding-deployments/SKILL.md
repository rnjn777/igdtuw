---
name: guarding-deployments
description: Prevents accidental or unsafe deployments by validating environment state and project health. Use when the user asks to deploy, release, or push to production.
---

# Guarding Deployments

## When to use this skill
- Before running deployment commands (e.g., `npm run deploy`, `aws s3 sync`).
- When the user mentions "staging", "production", or "release".
- After major refactors to ensure safety before shipping.

## Workflow
1. [ ] **Identify Target**: Determine the target environment (e.g., prod, staging).
2. [ ] **Validate Environment**: Run `scripts/check-env.sh <env>` to verify secrets.
3. [ ] **Verify Quality**: Run `./run-tests.sh` and ensure 100% pass rate.
4. [ ] **Check Branch**: Ensure current branch is `main` or `release/*` for production.
5. [ ] **Confirm with User**: Present a summary of checks and ask for final approval.

## Instructions
- **Safety First**: Never execute a destructive deployment command without first checking the local `.env` file for mismatched keys.
- **Template for Summary**:
    ```markdown
    ### Deployment Safety Report
    - **Branch**: `main` (Verified)
    - **Tests**: 42/42 Passed
    - **Env Audit**: No leaked keys found
    ```
- **Fragile Operations**: Always append `--dry-run` to commands if the user is hesitant.

## Resources
- [Environment Checker](scripts/check-env.sh)
- [Example Report](examples/sample-report.md)
