# ADR 0003: Use GitHub Actions and GHCR

## Context

The project required an automated CI/CD pipeline capable of testing, building, scanning, packaging, and deploying the application with minimal operational overhead.

## Decision

GitHub Actions was selected as the CI/CD platform and GitHub Container Registry (GHCR) was selected as the container registry. The workflow includes linting, testing, Trivy scanning, Gitleaks scanning, Syft SBOM generation, Docker image publishing, and automated Helm deployment.

## Consequences

The CI/CD pipeline became fully integrated with the GitHub ecosystem and avoided external registry credentials by using the built-in `GITHUB_TOKEN`. This simplified authentication and repository management. The tradeoff is tighter coupling to the GitHub platform.
