# ADR 0002: Use Helm for Kubernetes Deployment

## Context

The project required Kubernetes manifests for deployment, service exposure, ingress configuration, environment-specific values, and operational consistency between environments.

## Decision

Helm was selected to package Kubernetes resources and manage deployments. Separate values files (`values-dev.yaml` and `values-prod.yaml`) were used to support environment-specific configuration.

## Consequences

Helm simplified deployments, upgrades, and rollback operations. It also improved configuration management and reduced duplication between Kubernetes manifests. The tradeoff is the additional template structure and Helm-specific syntax complexity.
