# Initial source review

Date: 2026-10-11. This is an initial screening, not a full source audit or runtime test.

| Candidate | Proposed use | Caveats |
|---|---|---|
| Freqtrade | Primary isolated engine candidate | Mature Python engine, dry-run/backtesting and Binance support; GPL-3.0 requires a deliberate distribution/compliance decision. |
| Hummingbot | Alternative for connector/market-making workflows | Apache-2.0; strategy fit differs from retail spot automation. |
| CCXT | Optional exchange abstraction | Verify current license, supported endpoints, and exchange-specific behavior. |
| chrisleekr/binance-trading-bot | Ideas only, do not deploy unchanged | SECURITY.md reports plaintext secret storage and limited operator authentication. |
| GitLab AndreyPopov/spot-trading-bot | Further review candidate | Docker-first Binance Spot candidate; README says still under testing; GPL-3.0-or-later. |

## Selection principles
Do not copy whole repositories blindly. Prefer a process-isolated engine behind an authenticated API boundary, a separate UI, pinned dependencies, license inventory/SBOM, attribution, and CI. Strategy examples do not prove profitability.
