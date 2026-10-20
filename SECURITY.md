# Security Policy

## Reporting Security Issues

We take the security of this project and local agent workflows seriously. If you discover a vulnerability, prompt injection vector, or accidental data leakage issue, please report it privately:

- **Security Disclosure Contact:** Open an issue marked `[SECURITY]` or contact the maintainers directly.
- **Response Window:** We aim to acknowledge reports within 48 hours and provide a remediation plan within 5 business days.

## Agent Sandbox & Local Execution Principles

This repository starter provides behavioral constraints via `AGENTS.md` and `config/agent.local.yaml`, but **a prompt file is not an operating system sandbox**:
- Always run AI coding agents inside isolated user accounts, Docker containers, or virtual machines when executing untrusted scripts.
- Never commit `.env` or local configuration containing API keys or private endpoints.
- See [`docs/security.md`](./docs/security.md) for full operational security best practices.
