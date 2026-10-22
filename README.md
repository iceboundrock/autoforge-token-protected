# autoforge-token-protected (disposable)

Disposable fixture repository for the AutoForge fine-grained token
verification (iceboundrock/AutoForge#257, acceptance criterion 6).

Role: **PROTECTED_REPO**, the open merge gate. The `ci` workflow
(`.github/workflows/ci.yml`) runs on pushes to `main` and on pull requests,
using only the Python standard library and a read-only `GITHUB_TOKEN`.
`main` is meant to be protected by the `autoforge-token-verification`
ruleset: a pull request is required and so is the `ci` check.

The token probe (`probe.sh open`) creates, and may squash-merge, its own
`autoforge-probe-*` pull request here. Everything in this repository may be
deleted at any time. It holds no credentials, secrets or production data.
