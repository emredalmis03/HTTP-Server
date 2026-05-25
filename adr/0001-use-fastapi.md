# ADR 0001: Use FastAPI

## Context

The case study required a small HTTP application exposing simple endpoints such as `/ping`, `/healthz`, `/version`, and `/metrics`. The application also needed to work well inside a containerized Kubernetes environment and integrate easily with Prometheus metrics.

## Decision

FastAPI was selected as the application framework. It provides a lightweight development experience, simple endpoint definitions, built-in ASGI support, and easy integration with Prometheus instrumentation libraries.

## Consequences

The application remained small and easy to containerize. FastAPI also simplified health check endpoints and metrics exposure. The tradeoff is that the project intentionally stays minimal and does not include a larger production-oriented framework structure.
