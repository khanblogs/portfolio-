# Portfolio Transformation — Phase 1: Audit, Positioning, Direction
Prepared 2026-11-26 · Site audited: https://khanblogs.github.io/portfolio-/ (live) + local source
Status: FOR APPROVAL — no consequential change made yet under this brief.

## 1. Audit findings (measured, live site 2026-11-26)

### Performance
- HTML document = **868 KB**, of which **~745 KB is inline base64** (portrait photo + favicon). The portrait is the hero/LCP element: it cannot be cached, resized responsively, or prioritised — the single largest performance defect.
- HMS architecture image = **1.34 MB** PNG, unoptimized. Bada Business logo = 152 KB PNG shown at 30 px height.
- Four Google Font families now load (Fraunces, Sora, IBM Plex Sans, IBM Plex Mono) — needs subsetting/preload discipline in Phase 2.
- Server response itself is fast (~1 s total for HTML from test vantage); the weight, not the host, is the problem.

### SEO / discoverability
- **No sitemap.xml, no robots.txt, no custom 404** (all return 404 today).
- One page = one search-intent target. Case studies cannot rank or be shared individually.
- Present and correct: canonical URL, one JSON-LD Person block, meta description, OG tags. Title still leads with the old positioning ("Senior DevOps & MLOps Engineer").

### Structure / accessibility (source + rendered, desktop 1440 + mobile 390 screenshots reviewed)
- Good: single h1, semantic landmarks (header/nav/main/footer), lang="en", all 7 images have alt text, reduced-motion handling exists for the marquee.
- Gaps: **no skip link**; focus-visible states not verified; live-clock band updates every second (screen-reader noise risk — needs aria-hidden on the ticking numbers); contrast of muted text in light theme to be measured in Phase 4; marquee is decorative-duplicated content (aria handling to confirm).

### Conversion / journeys
- **No résumé download anywhere on the site** — the recruiter journey dead-ends at a mailto link. (A CV exists only as a LinkedIn Featured item.)
- No consulting entry point: services exist as a section, but there is no engagement scope, deliverables, process or client-specific CTA.
- CTO journey is the strongest today (9 detailed cases) but everything sits on one very long page; no flagship selection, no per-case URLs to share.

### What could not be inspected
- Real-user field data (no analytics/RUM by design), actual Google indexing state, and the repository's GitHub Pages build settings beyond what the live output shows.

## 2. Positioning (proposed)

**Primary positioning: Cloud & AI Platform Engineering** — supported by DevOps, SRE, MLOps, DevSecOps and FinOps.
Official employment titles stay untouched in Experience (Senior DevOps Engineer, NeGD / Digital India Corporation). No title inflation anywhere.

**Positioning statement (draft):**
"Cloud & AI Platform Engineer. I design and run the platforms AI products live on — Kubernetes estates, MLOps pipelines and self-hosted inference — for a national platform serving up to 100M users, regulated fintech, and startups across three continents."

**Three visitor journeys**
- Recruiter (10-second fit test): headline + 3 proof points + credentials strip → résumé download (DOCX/PDF) → contact.
- CTO/engineering leader (2-minute depth test): flagship case → architecture, decisions & alternatives, outcomes, limitations → related cases → contact.
- Business client: problem framing → engagement models & deliverables (consulting page) → process → start-a-conversation CTA.

## 3. Proposed sitemap (all under /portfolio-/)
- `/` — Home: positioning, proof points, 3 flagship cases, capability groups, credentials, experience summary, consulting teaser, contact.
- `/work/` — Case index (all nine).
- `/work/umang-platform/`, `/work/hms-voice-ai/`, `/work/azzy-agents/` — flagship case pages (full template: context, constraints, role, architecture, decisions & alternatives, implementation, measured outcome, limitations, lessons).
- `/work/<remaining six>/` — standard case pages, phased after flagships.
- `/consulting/` — Sarvnex entry point: problems solved, engagement models, deliverables, process, FAQ, CTA.
- `/assets/Shahrukh_Khan_Resume.pdf` + `.docx` — résumé downloads (linked from nav, home, contact).
- `404.html`, `sitemap.xml`, `robots.txt`.
Static, GitHub Pages, no server dependency, no tracking. Rollback = revert to current commit (bd225b5/fd6bf0e line) — the present one-pager stays deployable throughout.

## 4. Visual direction — "Living Infrastructure Atlas" (proposed)
- Deep ink/navy surfaces (evolution of the current identity), editorial serif display (Fraunces, added today) + Sora/IBM Plex text and mono annotations — like a premium technical publication.
- Accent decision for approval: current **gold** vs the brief's **restrained cyan/violet light**. Recommendation: keep gold as the brand metal, introduce cyan only as the "signal" colour inside the topology graphic. (Open decision D1.)
- Signature interactive: an **SVG platform topology** in the hero — Edge → API gateway → service mesh → data layer → ML model routing → observability loop. Nodes are real links to case studies; selecting a node shows a short factual caption. SVG-first (works without JS/WebGL, keyboard navigable, static fallback is the same graphic). No fake telemetry; motion is ambient only and honours reduced-motion. WebGL/Three.js assessed and **not** recommended — SVG achieves the concept at a fraction of the performance/accessibility cost.
- Architectural linework, disciplined spacing, generous margins; no scroll hijacking, no custom cursor (the brief forbids; today's cursor-glow will be removed in the rebuild), no glassmorphism overload.

## 5. Content-risk register (top items)
- R1 (High): **Organisation logos** added 2026-11-26 at the owner's verbal direction (DIC cropped emblem-free, UMANG, ZS, Aftershoot, Bada Business). Formal permission is not documented; the brief (§2) says do not use logos without appropriate permission. Decision needed: keep at owner's direction, or revert to text.
- R2 (High): **"100M monthly active users"** — UMANG's publicly cited figures are predominantly *registered* users; "monthly active" needs the owner's metric definition or softening to "platform serving up to 100M users". Case 01 also says "8–10 crore monthly users" and a diagram says "up to 100M MAU" — one consistent, defensible wording required.
- R3 (Medium): **99.95% / zero Sev-1** — must be framed as SLO target + incident record for a stated period, not a measured uptime guarantee.
- R4 (Medium): **Voice AI "100% field accuracy"** — true only as POC validation wording (controlled Hinglish dictations, 8 modules); must never read as production accuracy. Latency "~5 s" needs its conditions (warm model, CPU-only host, short dictation; end-to-end ≈ 55–60 s for a 33 s dictation).
- R5 (Medium): **"−30% infra spend / doubled capacity"** — owner's figure; needs scope + period in the claim register.
- R6 (Low): Case 01 dates the NeGD role "Nov 2025 – present" — chronology to confirm against the wider timeline (career start 2019 per photo card).
- R7 (Low): Consulting/Sarvnex copy must never imply NeGD/MeitY endorsement of private services.

## 6. Claim register
Started in `docs/CLAIM_REGISTER.md` — every prominent claim with original wording, source, proposed wording, metric definition, period, ownership, verification status. Unsupported items are marked OWNER-REVIEW and will not be silently published as fact.

## 7. Decisions requested
- D1: Accent — keep gold (+ cyan signal in topology) [recommended] / switch fully to cyan-violet.
- D2: Logos — keep at your direction / revert to text-only strip.
- D3: "100M" wording — define the metric (registered vs active) or adopt the softened wording.
- D4: Approve sitemap + flagship selection (UMANG, HMS Voice AI, Azzy Agents) and Phase 2 build.
