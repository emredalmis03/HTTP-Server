# Security Notes

This project includes several lightweight security practices appropriate for a small Kubernetes-based deployment.

---

# Container Security

Container images are scanned in CI using:

* Trivy vulnerability scanner
* Syft SBOM generation

The generated SBOM artifact is uploaded through GitHub Actions for inspection and dependency visibility.

---

# Secret Management

The repository does not contain hardcoded credentials.

Application configuration is managed through:

* Kubernetes ConfigMaps
* Kubernetes Secrets
* GitHub Actions Secrets and Variables

No AWS access key or long-lived registry credential is stored in the repository.

---

# Registry Authentication

GitHub Container Registry (GHCR) authentication is handled through the built-in `GITHUB_TOKEN` provided by GitHub Actions.

This avoids storing persistent container registry credentials.

---

# Repository Scanning

The CI pipeline includes:

* Gitleaks secret scanning
* Trivy image scanning

These checks help detect:

* accidental secret commits
* vulnerable dependencies
* insecure container images

---

# Kubernetes Security Considerations

The deployment includes:

* readiness probes
* liveness probes
* resource requests and limits
* PodDisruptionBudget

The application is deployed through Helm to improve deployment consistency and reduce manual configuration drift.

---

# Known Limitations

This project intentionally keeps the infrastructure lightweight to match the scope of the case study.

The following improvements could be added in a production-grade environment:

* NetworkPolicies
* TLS with cert-manager
* OIDC-based AWS authentication
* image signing with cosign
* Terraform/OpenTofu infrastructure provisioning
* dedicated secrets manager integration
* non-root container user
* stricter RBAC policies

---

# Reporting Security Issues

This repository was created for a technical case study and is not intended for public production use.

If a security issue is discovered, please open a private communication channel instead of creating a public issue.
