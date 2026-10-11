# Security Policy

## Prototype status
This repository currently contains a UI-only prototype. It does not connect to an exchange or save/transmit API keys. Do not enter real credentials in the prototype.

## Production requirements before enabling keys
- TLS only; secure HttpOnly SameSite cookies, session rotation, CSRF protection where applicable, rate limits and Argon2id password hashing.
- Server-side encryption for API credentials with the encryption key kept outside the database. Never return secret values after saving.
- No withdrawal permission on exchange keys; restrict keys to the server's stable outbound IP where supported.
- Separate exchange keys from data-provider and AI credentials.
- Validate symbol, precision, minimum notional, available balance, rate limits, slippage and order state before execution.
- Risk checks must not be bypassed by AI, strategy code, Telegram or manual signals.
- Default to BACKTEST/PAPER/DRY_RUN. LIVE requires explicit server-side security checks and human confirmation.
- Kill switch stops new entries and automation; it must not unexpectedly liquidate existing positions.
- Audit key changes, auth events, risk changes, mode changes and order lifecycle without recording secrets.
- Add dependency/SAST/secret/container scanning and authorization tests to CI; pin dependencies and test backup restoration.
