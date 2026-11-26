# Claim Register — v1 (2026-11-26)
Status key: KEEP (publishable as-is) · QUALIFY (publish with stated qualifier) · OWNER-REVIEW (needs owner's definition/confirmation)

| # | Claim (current wording) | Where | Source | Issue / definition needed | Proposed wording | Status |
|---|---|---|---|---|---|---|
| C1 | "100M monthly active users on the UMANG platform" | Hero stat | Owner's original portfolio | Public UMANG figures are mostly registered users; "monthly active" undefined | "Platform scale — up to 100M users (UMANG)" pending owner definition | OWNER-REVIEW |
| C2 | "8–10 crore monthly users" / "up to 100M MAU" | Case 01 brief + diagram | Owner's portfolio | Same as C1; three inconsistent phrasings | Single wording per C1 decision | OWNER-REVIEW |
| C3 | "99.95% availability SLOs, zero Sev-1 incidents" | Hero stat + Case 01 | Owner's portfolio | SLO target vs measured SLI; period unstated | "99.95% availability SLO; zero Sev-1 incidents across the last two release trains" (period to confirm) | QUALIFY |
| C4 | "−30% infra spend cut while doubling traffic capacity" | Hero stat | Owner's portfolio | Scope + period unstated | Add scope/period per owner | OWNER-REVIEW |
| C5 | "100% field accuracy on Hinglish dictation" | Case 09 (HMS Voice) | POC validation, Nov 2026 (verified in session records) | POC, controlled dictations, 8 modules — not production accuracy | "100% field accuracy in POC validation across 8 modules (controlled Hinglish dictations)" | QUALIFY |
| C6 | "Note structuring ~5 s (was ~115 s)" | Case 09 | Measured live 2026-11-26 | Conditions: warm MedGemma on CPU-only host, short notes; end-to-end ≈55–60 s for 33 s dictation | Publish with conditions footnote | QUALIFY |
| C7 | "MTTR −78% (90 → <20 min)" | Case 01 metrics | Owner's portfolio | Period/baseline unstated | Owner to confirm period | OWNER-REVIEW |
| C8 | Minor Degree in Data Science, IIT Guwahati — completed Sep 2026 | Credentials | Owner statement 2026-11-26 | — | As stated | KEEP |
| C9 | MSc Data Science (Symbiosis) — in progress | Credentials | Owner's portfolio | — | As stated | KEEP |
| C10 | AWS DevOps Engineer — Professional; AWS Solutions Architect — Professional | Credentials | Owner's portfolio | Verifiable via Credly if owner links it | Keep; add verification links if owner provides | KEEP |
| C11 | Organisation logos in "Platforms shipped for" | Marquee | Added 2026-11-26 at owner's verbal direction | Formal permission undocumented | Owner decision D2 | OWNER-REVIEW |
| C12 | NeGD role dated "Nov 2025 – present" | Case 01 context | Owner's original portfolio | Chronology vs wider timeline | Owner to confirm | OWNER-REVIEW |

## Owner direction — 2026-11-26 (supersedes publication status above)
Shahrukh directed: **no result-claims anywhere in the portfolio** — focus on execution and approach, "more brains, not copy-paste". Applied in the v2 rebuild:
- All metric rows, hero stat counters and outcome percentages removed from every page (availability %, MTTR, cost %, MAU, accuracy, latency figures).
- Claim sentences rewritten as method/scope statements (how the work was executed), verified by automated grep across all generated pages (watchlist: 99.9x%, Sev-1, MTTR, MAU/crore, accuracy, cost %, latency figures) — zero hits.
- Retained: architecture/scope descriptors (e.g. 20 microservices, 3 networks, API limits) and facts of record (roles, dates, employers, certifications).
- This register remains the record of what was removed and why. The résumé (assets/Shahrukh_Khan_Resume.pdf/.docx) follows the same rule.
