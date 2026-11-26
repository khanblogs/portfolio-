# -*- coding: utf-8 -*-
"""Portfolio v2 generator — Living Infrastructure Atlas (static, GitHub Pages /portfolio-/)."""
import json, re, os

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE = '/portfolio-/'
cases = json.load(open(f'{ROOT}/src/cases.json'))
def frag(name):
    return open(f'{ROOT}/src/{name}.html', encoding='utf-8').read()

FONTS = ('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;0,9..144,700;1,9..144,500'
         '&family=Sora:wght@500;600;700;800&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@400;500;600&display=swap')

def head(title, desc, path, extra_jsonld=''):
    canon = 'https://khanblogs.github.io' + BASE + path
    return f'''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{title}</title>
    <meta name="description" content="{desc}" />
    <meta name="author" content="Shahrukh Khan" />
    <meta name="robots" content="index, follow" />
    <link rel="canonical" href="{canon}" />
    <meta name="theme-color" content="#0b0d10" />
    <meta property="og:type" content="website" />
    <meta property="og:title" content="{title}" />
    <meta property="og:description" content="{desc}" />
    <meta property="og:url" content="{canon}" />
    <meta property="og:image" content="https://khanblogs.github.io{BASE}assets/og-image.png" />
    <meta name="twitter:card" content="summary_large_image" />
    <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='12' fill='%230d1b34'/%3E%3Ctext x='32' y='45' font-family='Arial' font-size='36' font-weight='bold' fill='%23d4b77a' text-anchor='middle'%3ES%3C/text%3E%3C/svg%3E" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="{FONTS}" rel="stylesheet" />
    <link rel="stylesheet" href="{BASE}assets/site.css" />
    <link rel="stylesheet" href="{BASE}assets/v2.css" />
    {extra_jsonld}
  </head>
  <body>
    <a class="skip" href="#main">Skip to content</a>
    <div id="progressBar" aria-hidden="true"></div>
'''

NAV = f'''
    <header class="nav"><div class="wrap nav-in">
      <a class="nav-name" href="{BASE}">Shahrukh Khan<span style="color:var(--accent)">.</span></a>
      <nav class="nav-links" aria-label="Primary">
        <a href="{BASE}work/">Work</a>
        <a href="{BASE}#services">Services</a>
        <a href="{BASE}#stack">Stack</a>
        <a href="{BASE}#credentials">Credentials</a>
        <a href="{BASE}#experience">Experience</a>
        <a href="{BASE}consulting/">Consulting</a>
      </nav>
      <a class="btn btn-primary nav-cta" href="{BASE}assets/Shahrukh_Khan_Resume.pdf" download>Résumé ↓</a>
      <button class="nav-burger" aria-label="Menu" aria-expanded="false" onclick="document.body.classList.toggle('menu-open');this.setAttribute('aria-expanded',document.body.classList.contains('menu-open'))">☰</button>
    </div></header>
'''

FOOT = f'''
    <footer class="foot"><div class="wrap foot-in">
      <div>© 2026 Shahrukh Khan · New Delhi, India</div>
      <div class="foot-links">
        <a href="{BASE}work/">Work</a><a href="{BASE}consulting/">Consulting</a>
        <a href="{BASE}assets/Shahrukh_Khan_Resume.pdf" download>Résumé (PDF)</a>
        <a href="https://www.linkedin.com/in/shahrukhkhan-devops" rel="noopener">LinkedIn</a>
        <a href="https://github.com/khanblogs" rel="noopener">GitHub</a>
        <a href="mailto:iamdevopskhan@gmail.com">Email</a>
      </div>
    </div></footer>
    <button id="toTop" aria-label="Back to top" title="Back to top">↑</button>
    <script src="{BASE}assets/site.js" defer></script>
  </body>
</html>
'''

PERSON_LD = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"ProfilePage","mainEntity":{"@type":"Person","name":"Shahrukh Khan",
"jobTitle":"Senior DevOps Engineer","description":"Cloud & AI Platform Engineer — Kubernetes, MLOps and self-hosted AI platforms for national-scale government systems, fintech and startups.",
"url":"https://khanblogs.github.io/portfolio-/","email":"mailto:iamdevopskhan@gmail.com",
"address":{"@type":"PostalAddress","addressLocality":"New Delhi","addressCountry":"IN"},
"worksFor":{"@type":"Organization","name":"Digital India Corporation (NeGD), MeitY"},
"alumniOf":[{"@type":"CollegeOrUniversity","name":"IIT Guwahati"},{"@type":"CollegeOrUniversity","name":"Symbiosis International University"},{"@type":"CollegeOrUniversity","name":"University of Delhi"}],
"sameAs":["https://www.linkedin.com/in/shahrukhkhan-devops","https://github.com/khanblogs"],
"knowsAbout":["Cloud Platform Engineering","DevOps","Site Reliability Engineering","MLOps","DevSecOps","FinOps","Kubernetes","Terraform","AWS","Microsoft Azure","Google Cloud","AI Agents","LLMOps"]}}
</script>'''

def page(title, desc, path, body, ld=''):
    return head(title, desc, path, ld) + NAV + f'<main id="main">{body}</main>' + FOOT

def write(rel, content):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(content)
    print('wrote', rel, len(content)//1024, 'KB')

# ---------------- Case metadata ----------------
SLUGS = {
    '01': ('umang-platform', 'Flagship · National platform'),
    '02': ('fintech-aws-migration', 'Fintech · Migration'),
    '03': ('bank-statement-analyzer-mlops', 'Fintech · MLOps'),
    '04': ('azure-gcp-replatforming', 'Re-platforming'),
    '05': ('azzy-agents', 'Flagship · AI platform'),
    '06': ('pbm-portal', 'Government · Finance platform'),
    '07': ('umangverse', 'Government · Web experience'),
    '08': ('government-production-fleet', 'Government · Operations'),
    '09': ('hms-voice-ai', 'Flagship · Healthcare AI'),
}
ONELINERS = {
    '01': 'Owning the AWS platform behind UMANG — hybrid EKS + ECS, multi-AZ Envoy ingress, KEDA autoscaling and SLO-gated releases.',
    '02': 'Active-active EKS migration for a regulated fintech — weighted traffic shifts, reversible at every step.',
    '03': 'Production ML for credit decisioning: FastAPI inference, Airflow pipelines, MLflow registry, Kubernetes autoscaling.',
    '04': 'Azure → GCP re-platforming on GKE — endpoint parity verified service-by-service before cutover, Istio mesh for traffic policy.',
    '05': 'A self-hosted AI agent platform: provider-agnostic LLM gateway with failover, local embeddings, agents that run real operations.',
    '06': 'Ministry of Finance portal from staging chaos to audited NGC production — bulk AI summaries, VAPT/SAST closure, weekly backups.',
    '07': 'An immersive web experience for the UMANG ecosystem — designed, built and set up end-to-end, SAST-reviewed.',
    '08': 'One secure operating model across NFS (NITI Aayog), UPMS, MoSPI and a 20-microservice hospital platform.',
    '09': 'Doctors dictate in Hinglish; self-hosted AI writes the structured note. Confirm-before-save, audio never leaves the hospital.',
}
FLAGSHIPS = ['01', '09', '05']

EXTRAS = {
'01': '''
            <div class="hld reveal"><span class="kicker no-bar mono" style="font-size:11.5px;color:var(--accent);letter-spacing:0.14em;">KEY DECISIONS &amp; ALTERNATIVES</span>
              <div class="hld-notes">
                <div class="hld-note"><strong>Hybrid EKS + ECS, not a big-bang replatform</strong>A national citizen service cannot pause. New workloads land on EKS while stable services stay on ECS — migration risk is taken in slices, never all at once.</div>
                <div class="hld-note"><strong>Error-budget release gates</strong>Releases are gated on measured SLOs and error budgets, not calendar pressure — the mechanism that keeps release trains boring, in the best sense.</div>
                <div class="hld-note"><strong>KEDA event-driven autoscaling</strong>Citizen traffic spikes around government deadlines; scaling follows events and queues, not just CPU averages.</div>
              </div></div>
            <div class="hld reveal"><span class="kicker no-bar mono" style="font-size:11.5px;color:var(--accent);letter-spacing:0.14em;">LIMITATIONS &amp; LESSONS</span>
              <div class="hld-notes">
                <div class="hld-note"><strong>Limitations</strong>Platform-level metrics are team outcomes on a shared national platform; change windows are governed by multiple stakeholders, which trades speed for safety.</div>
                <div class="hld-note"><strong>Lesson</strong>Observability before automation: incident response improved when telemetry and runbooks were standardised across services — shared signals, not more tooling.</div>
                <div class="hld-note"><strong>Lesson</strong>An error budget is a negotiation tool — it turns "ship vs stability" arguments into arithmetic.</div>
              </div></div>''',
'09': '''
            <div class="hld reveal"><span class="kicker no-bar mono" style="font-size:11.5px;color:var(--accent);letter-spacing:0.14em;">KEY DECISIONS &amp; ALTERNATIVES</span>
              <div class="hld-notes">
                <div class="hld-note"><strong>Self-hosted open-source models, not cloud AI APIs</strong>Cloud speech/LLM APIs were rejected on data-residency grounds: patient audio must never leave the hospital. Whisper + MedGemma + Kokoro run on hospital hardware, with no licence cost and no external API in the path.</div>
                <div class="hld-note"><strong>Confirm-before-save as architecture</strong>The clinician-confirmation gate is built into the data path, not a UI preference — nothing reaches the record unreviewed.</div>
                <div class="hld-note"><strong>Isolated POC first</strong>The stack proved itself in a separate compose project and database beside the live HMS; only validated modules were integrated. A larger model (Qwen3-8B) was evaluated and rejected — it exceeded the ~6 GB POC memory budget.</div>
              </div></div>
            <div class="hld reveal"><span class="kicker no-bar mono" style="font-size:11.5px;color:var(--accent);letter-spacing:0.14em;">LIMITATIONS &amp; LESSONS</span>
              <div class="hld-notes">
                <div class="hld-note"><strong>Performance is an inference problem</strong>The latency work lived in the inference path: keeping the model warm, trimming decoding parameters, parallelising transcription on a CPU-only host. A GPU node is the documented scaling path when volume demands it.</div>
                <div class="hld-note"><strong>Known limitation</strong>Whisper can garble Hindi numerals in fast speech — the editable transcript review exists precisely for this.</div>
                <div class="hld-note"><strong>Lesson</strong>In clinical AI, the trust feature is the gate, not the model. Adoption followed the confirm step, not the demo.</div>
              </div></div>''',
'05': '''
            <div class="hld reveal"><span class="kicker no-bar mono" style="font-size:11.5px;color:var(--accent);letter-spacing:0.14em;">KEY DECISIONS &amp; ALTERNATIVES</span>
              <div class="hld-notes">
                <div class="hld-note"><strong>Provider-agnostic gateway, not direct SDKs</strong>All inference routes through OmniRoute + freellmapi, so models are swappable parts with a cost-optimised failover chain — no vendor lock-in at the agent layer.</div>
                <div class="hld-note"><strong>Local embeddings in PostgreSQL + pgvector</strong>Retrieval stays self-hosted instead of an external vector SaaS — one less dependency, one less data egress.</div>
                <div class="hld-note"><strong>Compose on one node, deliberately</strong>At current scale a disciplined Docker Compose stack beats operating Kubernetes for a personal platform — the complexity budget is spent on the agents, not the substrate.</div>
              </div></div>
            <div class="hld reveal"><span class="kicker no-bar mono" style="font-size:11.5px;color:var(--accent);letter-spacing:0.14em;">LIMITATIONS &amp; LESSONS</span>
              <div class="hld-notes">
                <div class="hld-note"><strong>Limitations</strong>Single-node deployment is not high-availability, and the cost strategy leans on free model tiers — a production client deployment would pin paid models behind the same gateway.</div>
                <div class="hld-note"><strong>Lesson</strong>Failover is a product feature: the day a free model degraded, the chain absorbed it and no agent task failed.</div>
                <div class="hld-note"><strong>Lesson</strong>Memory quality beats model size — curated local embeddings improved agent answers more than a bigger LLM did.</div>
              </div></div>''',
}

# ---------------- Interactive topology (SVG, links are real) ----------------
TOPOLOGY = f'''
      <section class="topo-sec" aria-label="Platform topology — selected architecture map">
        <div class="wrap">
          <div class="section-head reveal">
            <span class="kicker no-bar mono" style="display:block;margin-bottom:6px;color:var(--accent);letter-spacing:0.12em;">THE ATLAS</span>
            <h2>One map of the platforms.</h2>
            <p class="lede">Every node below is a real system from the case studies. Select a node to see what it does — and where it is proven.</p>
          </div>
          <figure class="diagram topo reveal" style="margin:0">
            <svg class="dg" viewBox="0 0 1040 360" role="group" aria-label="Interactive platform topology: edge and ingress routes to an API gateway, a Kubernetes platform and data layer, with ML model routing and an observability loop">
              <defs>
                <marker id="ta" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" style="fill:var(--soft)"/></marker>
                <marker id="taa" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" style="fill:#22d3ee"/></marker>
              </defs>
              <a href="{BASE}work/umang-platform/" class="tnode" data-cap="Edge &amp; ingress — multi-AZ Envoy fronting a national citizen platform; TLS and traffic policy at one controlled door. Proven in the UMANG case study.">
                <rect class="box" x="8" y="120" width="168" height="92" /><text x="92" y="158" text-anchor="middle">edge &amp; ingress</text><text class="sub" x="92" y="180" text-anchor="middle">Envoy · multi-AZ · TLS</text></a>
              <a href="{BASE}work/hms-voice-ai/" class="tnode" data-cap="API gateway — one authenticated entry to 20 microservices (YARP), injecting identity and tenant context into every call. Proven in the HMS Voice AI case study.">
                <rect class="box" x="224" y="120" width="168" height="92" /><text x="308" y="158" text-anchor="middle">API gateway</text><text class="sub" x="308" y="180" text-anchor="middle">YARP · JWT · tenancy</text></a>
              <a href="{BASE}work/umang-platform/" class="tnode" data-cap="Kubernetes platform — hybrid EKS + ECS estate, KEDA autoscaling, SLO-gated releases scaled on events, released through SLO gates. Proven in the UMANG case study.">
                <rect class="box-hl" x="440" y="120" width="184" height="92" /><text x="532" y="158" text-anchor="middle">Kubernetes platform</text><text class="sub" x="532" y="180" text-anchor="middle" style="fill:var(--accent)">EKS + ECS · KEDA · GitOps</text></a>
              <a href="{BASE}work/azzy-agents/" class="tnode" data-cap="Data &amp; state — PostgreSQL + pgvector and Redis: sessions, queues, memory and vectors for the agent platform. Proven in the Azzy Agents case study.">
                <rect class="box" x="672" y="120" width="168" height="92" /><text x="756" y="158" text-anchor="middle">data &amp; state</text><text class="sub" x="756" y="180" text-anchor="middle">PostgreSQL · pgvector · Redis</text></a>
              <a href="{BASE}work/azzy-agents/" class="tnode" data-cap="ML model routing — a provider-agnostic gateway with a failover chain across models; self-hosted inference where data residency demands it. Proven in Azzy Agents and HMS Voice AI.">
                <rect class="box sig" x="440" y="252" width="184" height="84" /><text x="532" y="286" text-anchor="middle">ML model routing</text><text class="sub" x="532" y="308" text-anchor="middle">gateway · failover · local LLMs</text></a>
              <a href="{BASE}work/umang-platform/" class="tnode" data-cap="Observability loop — OpenTelemetry, Prometheus and Grafana feeding SLOs, error budgets and shared runbooks across the estate. Proven in the UMANG case study.">
                <rect class="box sig" x="672" y="252" width="168" height="84" /><text x="756" y="286" text-anchor="middle">observability</text><text class="sub" x="756" y="308" text-anchor="middle">OTel · Prometheus · Grafana</text></a>
              <rect class="box" x="440" y="24" width="184" height="64" /><text x="532" y="52" text-anchor="middle">citizens &amp; clients</text><text class="sub" x="532" y="72" text-anchor="middle">web · mobile · APIs</text>
              <path class="edge" d="M176,166 H220" marker-end="url(#ta)"/>
              <path class="edge" d="M392,166 H436" marker-end="url(#ta)"/>
              <path class="edge" d="M624,166 H668" marker-end="url(#ta)"/>
              <path class="edge" d="M532,88 V116" marker-end="url(#ta)"/>
              <path class="edge-hl" style="stroke:#22d3ee" d="M532,212 V248" marker-end="url(#taa)"/>
              <path class="edge-hl" style="stroke:#22d3ee" d="M624,294 H668" marker-end="url(#taa)"/>
              <path class="edge" d="M756,252 V216" marker-end="url(#ta)"/>
            </svg>
            <figcaption id="topoCap" aria-live="polite">Select any node — each one opens the case study where that layer is proven in production.</figcaption>
          </figure>
          <noscript><p class="lede" style="margin-top:12px">The nodes above are direct links to case studies; no JavaScript is required to use this map.</p></noscript>
        </div>
      </section>
'''

# ---------------- Home ----------------
def marquee():
    items = '''<span class="logo-item"><span class="logo-card"><img src="''' + BASE + '''assets/logos/digital-india.png" alt="Digital India Corporation" loading="lazy" /></span></span>
            <span class="logo-item"><span class="logo-card"><img src="''' + BASE + '''assets/logos/umang.webp" alt="UMANG" style="height:34px" loading="lazy" /><span class="lw">UMANG</span></span></span>
            <span>NITI Aayog (UPMS · NITI For States · NGO Darpan)</span>
            <span>Creditech Solutions (AlphaMoney)</span>
            <span>AlphaCorp · Alpha Design Studio</span>
            <span>Smartvizx</span>
            <span>SignCatch (SKY Inno Labs)</span>
            <span>Servando Technologies (Boston)</span>
            <span class="logo-item"><span class="logo-card"><img src="''' + BASE + '''assets/logos/zs.svg" alt="ZS Associates" loading="lazy" /></span></span>
            <span class="logo-item"><span class="logo-card"><img src="''' + BASE + '''assets/logos/aftershoot.webp" alt="Aftershoot" loading="lazy" /></span></span>
            <span class="logo-item"><span class="logo-card"><img src="''' + BASE + '''assets/logos/badabusiness.webp" alt="Bada Business" loading="lazy" /></span></span>
            <span>Enterprise Monkey</span>'''
    return f'''
      <div class="marquee-zone" aria-label="Organisations Shahrukh has worked with">
        <div class="label">Platforms shipped for</div>
        <div class="marquee"><div class="marquee-track" id="marqueeTrack">{items}</div></div>
      </div>'''

APPROACH = '''
      <section class="approach-sec" aria-label="How Shahrukh works">
        <div class="wrap">
          <div class="section-head reveal">
            <span class="kicker no-bar mono" style="display:block;margin-bottom:6px;color:var(--accent);letter-spacing:0.12em;">THE APPROACH</span>
            <h2>Execution is the portfolio.</h2>
            <p class="lede">Numbers age; method compounds. Four habits run through every engagement below — they are why the outcomes happened, and they are what you actually hire.</p>
          </div>
          <div class="approach-grid">
            <div class="approach-card reveal"><div class="a-num">01</div><h3>Prove it in isolation first</h3><p>New systems earn trust beside the live one, not inside it — a separate stack, a separate database, real validation. The HMS Voice AI ran as an isolated POC until eight modules passed; only then did integration begin.</p></div>
            <div class="approach-card reveal" data-delay="1"><div class="a-num">02</div><h3>Gate on evidence, not dates</h3><p>Releases move when SLOs, error budgets and security scans say so. On UMANG that discipline — not heroics — is what the release trains run on.</p></div>
            <div class="approach-card reveal" data-delay="2"><div class="a-num">03</div><h3>Build before you tear down</h3><p>New images are built and verified before old ones stop; every deploy carries a named rollback. Migrations run active-active with weighted traffic shifts — zero-downtime is a procedure, not a hope.</p></div>
            <div class="approach-card reveal" data-delay="3"><div class="a-num">04</div><h3>Leave it operable</h3><p>Runbooks, backups with restore drills, dated release branches, documented decisions. A platform is finished when someone else can run it at 3 a.m. — that is the standard every handover below was held to.</p></div>
          </div>
        </div>
      </section>'''

def flagship_cards():
    cards = ''
    for n in FLAGSHIPS:
        c = next(x for x in cases if x['n'] == n)
        slug, tag = SLUGS[n]
        cards += f'''
            <a class="flag-card reveal" href="{BASE}work/{slug}/">
              <div class="f-tag mono">{tag}</div>
              <h3>{c['title']}</h3>
              <p>{ONELINERS[n]}</p>
              <span class="f-link">Read the case study →</span>
            </a>'''
    return f'''
      <section class="flag-sec" aria-label="Flagship case studies">
        <div class="wrap">
          <div class="section-head reveal">
            <span class="kicker no-bar mono" style="display:block;margin-bottom:6px;color:var(--accent);letter-spacing:0.12em;">01 — FLAGSHIP WORK</span>
            <h2>Three engagements, in depth.</h2>
            <p class="lede">Context, constraints, architecture, the decisions and their alternatives, measured outcomes — and the limitations, stated plainly.</p>
          </div>
          <div class="flag-grid">{cards}</div>
          <p style="margin-top:22px"><a class="btn btn-ghost" href="{BASE}work/">All nine case studies <span class="arr">→</span></a></p>
        </div>
      </section>'''

TZ = '''
      <div class="tz-band" aria-label="Working across global time zones">
        <div class="label">Based in New Delhi — working across global time zones</div>
        <div class="tz-row" id="tzRow">
          <div class="tz-cell home"><div class="c">New Delhi · IST</div><div class="t" data-tz="Asia/Kolkata" aria-hidden="true">--:--</div></div>
          <div class="tz-cell"><div class="c">Dubai</div><div class="t" data-tz="Asia/Dubai" aria-hidden="true">--:--</div></div>
          <div class="tz-cell"><div class="c">Berlin</div><div class="t" data-tz="Europe/Berlin" aria-hidden="true">--:--</div></div>
          <div class="tz-cell"><div class="c">London</div><div class="t" data-tz="Europe/London" aria-hidden="true">--:--</div></div>
          <div class="tz-cell"><div class="c">Toronto</div><div class="t" data-tz="America/Toronto" aria-hidden="true">--:--</div></div>
          <div class="tz-cell"><div class="c">Auckland</div><div class="t" data-tz="Pacific/Auckland" aria-hidden="true">--:--</div></div>
        </div>
      </div>'''

def home_body():
    hero = f'''
      <section class="hero" style="padding-top: clamp(56px, 7vw, 96px)">
        <div class="aurora" aria-hidden="true"><i></i><i></i><i></i></div><div id="cursorGlow" aria-hidden="true"></div>
        <div class="hero-fade"></div>
        <div class="wrap hero-grid">
          <div>
            <span class="status reveal"><span class="pulse"></span> Open to senior DevOps / platform roles · Remote worldwide · Relocation-ready</span>
            <h1 class="reveal" data-delay="1">
              <span class="thin">Shahrukh Khan — Senior DevOps · MLOps · Platform Engineer</span>
              <span class="shine">Cloud &amp; AI platforms, engineered for national scale.</span>
            </h1>
            <p class="hero-sub reveal" data-delay="2">
              I design and run the platforms AI products live on — Kubernetes estates, MLOps pipelines and
              self-hosted inference. Today that is the <strong>AWS platform behind UMANG</strong>, India's national
              super-app — alongside production platforms for
              ministries, regulated fintech and startups. The method matters more than the metrics: prove in
              isolation, gate on evidence, build before teardown, leave everything operable.
            </p>
            <div class="hero-ctas reveal" data-delay="3">
              <a class="btn btn-primary" href="{BASE}work/">Explore the work <span class="arr">↓</span></a>
              <a class="btn btn-ghost" href="{BASE}assets/Shahrukh_Khan_Resume.pdf" download>Download résumé <span class="arr">↓</span></a>
              <a class="btn btn-ghost" href="mailto:iamdevopskhan@gmail.com?subject=Project%20inquiry%20via%20portfolio">Discuss a project <span class="arr">→</span></a>
            </div>
            <div class="hero-note reveal" data-delay="3">Eight years across government platforms, regulated fintech, startups and international consulting — the work below is documented as it was executed: context, constraints, decisions, and what they cost.</div>
          </div>
          <div class="reveal" data-delay="2">
            <div class="photo-card">
              <img src="{BASE}assets/portrait.webp" srcset="{BASE}assets/portrait-480.webp 480w, {BASE}assets/portrait.webp 900w" sizes="(max-width: 700px) 90vw, 460px" alt="Portrait of Shahrukh Khan, Senior DevOps Engineer" width="900" height="1125" fetchpriority="high" />
              <span class="corner">SINCE 2019</span>
              <div class="photo-chip">
                <span class="role"><strong>Shahrukh Khan</strong>Senior DevOps · MLOps · Platform</span>
                <span class="tz">New Delhi · IST</span>
              </div>
            </div>
          </div>
        </div>
      </section>'''
    consulting_teaser = f'''
      <section class="consult-teaser" aria-label="Consulting">
        <div class="wrap">
          <div class="teaser-card reveal">
            <div>
              <span class="kicker no-bar mono" style="font-size:11.5px;color:var(--accent);letter-spacing:0.14em;">CONSULTING — SARVNEX TECHNOLOGIES</span>
              <h2>Have a platform problem instead of a vacancy?</h2>
              <p>Fixed-scope engagements for cloud reliability, cost, and AI deployment — assessed first, quoted honestly, executed with the same gates I run in production.</p>
            </div>
            <a class="btn btn-primary" href="{BASE}consulting/">See how engagements work <span class="arr">→</span></a>
          </div>
        </div>
      </section>'''
    return (hero + marquee() + APPROACH + TOPOLOGY + flagship_cards()
            + scrub(frag('services')) + frag('stack') + frag('credentials') + scrub(frag('experience'))
            + TZ + consulting_teaser + frag('contact'))

# home write moved to end (scrub defined later)

# ---------------- Claim scrubber (owner direction 2026-11-26: no result-claims) ----------------
def drop_block(html, marker):
    """Remove the <div ...> block starting at marker, depth-aware."""
    i = html.find(marker)
    if i < 0:
        return html
    start = html.rfind('<div', 0, i)
    depth, j = 0, start
    while True:
        nxt_open = html.find('<div', j)
        nxt_close = html.find('</div>', j)
        if nxt_close < 0:
            return html
        if 0 <= nxt_open < nxt_close:
            depth += 1; j = nxt_open + 4
        else:
            depth -= 1; j = nxt_close + 6
            if depth == 0:
                return html[:start] + html[j:]

PHRASE_FIXES = [
    # Case 01
    ('Sustained 99.95% availability across two release trains with zero Sev-1 incidents on a hybrid EKS + ECS estate, multi-AZ Envoy ingress, KEDA-driven autoscaling, and SLO / error-budget release gates',
     'Run the hybrid EKS + ECS estate behind multi-AZ Envoy ingress, with KEDA-driven autoscaling and releases gated on SLOs and error budgets rather than calendar dates'),
    ('Cut MTTR from ~90 minutes to under 20 minutes across 40+ microservices — including integrations with EPFO, DigiYatra, DigiLocker and NSSO — by standardizing OpenTelemetry instrumentation and shared SRE runbooks',
     'Standardised OpenTelemetry instrumentation and shared SRE runbooks across the microservice estate — including integrations with EPFO, DigiYatra, DigiLocker and NSSO — so incidents are diagnosed from shared signals, not tribal knowledge'),
    # Case 02
    ('Delivered a zero-downtime migration — zero customer-impacting minutes, 99.9% post-migration SLO — via active-active EKS with Route 53 weighted traffic shifts and Terraform-managed landing zones',
     'Executed the migration as an active-active EKS move with Route 53 weighted traffic shifts and Terraform-managed landing zones — traffic moved in measured, reversible steps'),
    ('Cut infrastructure cost by 30% while doubling traffic capacity : replaced manual provisioning with reusable Terraform modules, Karpenter-driven node consolidation, and right-sized RDS PostgreSQL tiers',
     'Replaced manual provisioning with reusable Terraform modules, Karpenter-driven node consolidation and right-sized RDS PostgreSQL tiers — cost treated as an architectural input, reviewed at every release'),
    ('Cut infrastructure cost by 30% while doubling traffic capacity', 'Rebuilt provisioning around reusable Terraform modules and Karpenter-driven consolidation'),
    # Case 03
    ('ingesting and classifying thousands of statements daily', 'ingesting and classifying bank statements'),
    ('an 8-week Kubeflow + MLflow real-time and batch inference HLD/LLD', 'a Kubeflow + MLflow real-time and batch inference HLD/LLD'),
    # Case 04
    ('Closed the Azure → GCP migration ahead of deadline with zero data loss and 100% endpoint parity : workloads re-platformed on GKE , pipelines rebuilt on Cloud Build , and keyless service auth via Workload Identity .',
     'Re-platformed the workloads onto GKE, pipelines rebuilt on Cloud Build, and keyless service auth via Workload Identity — endpoint parity verified service-by-service before cutover'),
    ('Closed the Azure → GCP migration ahead of deadline with zero data loss and 100% endpoint parity', 'Re-platformed the workloads onto GKE, verifying endpoint parity service-by-service before cutover'),
    ('Improved p95 latency by ~35% by introducing the Istio service mesh — mTLS, per-route retry/timeout policies, and deliberate traffic shaping',
     'Introduced the Istio service mesh — mTLS, per-route retry/timeout policies, and deliberate traffic shaping — so latency behaviour became a policy, not an accident'),
    # Case 09
    ('passing validation across EMR, OPD, Pathology, Radiology, Pharmacy, Billing, IPD and Discharge with 100% field accuracy on Hinglish dictation',
     'validated module-by-module across EMR, OPD, Pathology, Radiology, Pharmacy, Billing, IPD and Discharge on Hinglish dictation'),
    ('Performance-tuned in production: note structuring went from ~115 seconds to ~5 seconds (warm model, tuned inference); a 33-second dictation is review-ready in about a minute.',
     'Performance work centred on the inference path: keeping the model warm, trimming decoding parameters and parallelising transcription, until dictation felt like a tool rather than a wait.'),
    ('POC cost: ₹0. Every component is free and open-source, self-hosted.',
     'Every component is free and open-source, self-hosted.'),
    ('POC cost: ₹0.', 'Every component is free and open-source.'),
]


def flex(html, phrase, repl):
    """Replace a phrase even when HTML tags sit between its words."""
    pat = r'(?:\s|<[^>]+>)+'.join(re.escape(w) for w in phrase.split(' '))
    return re.sub(pat, repl, html)

FLEX_FIXES = [
    ('Sustained 99.95% availability across two release trains with zero Sev-1 incidents on a hybrid EKS + ECS estate, multi-AZ Envoy ingress, KEDA-driven autoscaling, and SLO/error-budget release gates',
     'Run the hybrid EKS + ECS estate behind multi-AZ Envoy ingress, with KEDA-driven autoscaling and releases gated on SLOs and error budgets rather than calendar dates'),
    ('Cut MTTR from ~90 minutes to under 20 minutes across 40+ microservices — including integrations with EPFO, DigiYatra, DigiLocker and NSSO — by standardizing OpenTelemetry instrumentation and shared SRE runbooks',
     'Standardised OpenTelemetry instrumentation and shared SRE runbooks across the microservice estate — including integrations with EPFO, DigiYatra, DigiLocker and NSSO — so incidents are diagnosed from shared signals, not tribal knowledge'),
    ('Delivered a zero-downtime migration — zero customer-impacting minutes, 99.9% post-migration SLO — via active-active EKS with Route 53 weighted shifts and Terraform-managed landing zones',
     'Executed the migration as an active-active EKS move with Route 53 weighted traffic shifts and Terraform-managed landing zones — traffic moved in measured, reversible steps'),
    ('Cut infrastructure cost by 30% while doubling traffic capacity: replaced manual provisioning with reusable Terraform modules, Karpenter-driven node consolidation, and right-sized RDS PostgreSQL tiers',
     'Replaced manual provisioning with reusable Terraform modules, Karpenter-driven node consolidation and right-sized RDS PostgreSQL tiers — cost treated as an architectural input, reviewed at every release'),
    ('Closed the Azure → GCP migration ahead of deadline with zero data loss and 100% endpoint parity: workloads re-platformed on GKE, pipelines rebuilt on Cloud Build, and Workload Identity for keyless auth',
     'Re-platformed the workloads onto GKE with pipelines rebuilt on Cloud Build and Workload Identity for keyless auth — endpoint parity verified service-by-service before cutover'),
    ('Improved p95 latency by ~35% by introducing the Istio service mesh — mTLS, per-route retry/timeout policies, and deliberate traffic shaping',
     'Introduced the Istio service mesh — mTLS, per-route retry/timeout policies, and deliberate traffic shaping — so latency behaviour became a policy, not an accident'),
    ('passing validation across EMR, OPD, Pathology, Radiology, Pharmacy, Billing, IPD and Discharge — with 100% field accuracy on Hinglish dictation',
     'validated module-by-module across EMR, OPD, Pathology, Radiology, Pharmacy, Billing, IPD and Discharge on Hinglish dictation'),
    ('Performance-tuned in production: note structuring went from ~115 seconds to ~5 seconds (warm model, tuned inference); a 33-second dictation is review-ready in about a minute.',
     'Performance work centred on the inference path: keeping the model warm, trimming decoding parameters and parallelising transcription, until dictation felt like a tool rather than a wait.'),
    # experience fragment
    ('at up to 100M MAU, sustained 99.95% availability and zero Sev-1;', ';'),
    ('MyScheme integration with zero downtime', 'MyScheme integration into the UMANG app'),
    ('Zero-downtime AWS migration (99.9% SLO); −30% infra cost while doubling capacity;', 'AWS migration executed active-active with weighted traffic shifts; Terraform and Karpenter platform rebuild;'),
    ('Azure → GCP migration closed ahead of deadline with zero data loss; p95 latency improved ~35% via the Istio service mesh.',
     'Azure → GCP re-platforming onto GKE; Istio service mesh for mTLS and per-route traffic policy.'),
    ('AWS → Azure migration of a microservices estate with no functional regressions; mean deployment time cut ~60% via standardized Helm and shared CI pipelines.',
     'AWS → Azure migration of a microservices estate onto AKS; standardised Helm charts and a shared CI pipeline across the estate.'),
    ('Reduced manual administrative effort 30% across the eGov Samarth ERP rollout with Bash/Python automation and UiPath-orchestrated workflows.',
     'Automated provisioning, backup and routine operations across the eGov Samarth ERP rollout — Bash/Python scripting and UiPath-orchestrated workflows.'),
    # services fragment
    ('Traffic-shifted cutover with 99.9%+ SLO targets', 'Traffic-shifted cutover with rehearsed rollback'),
    ('Past engagements: −30% infra spend while doubling traffic capacity, Karpenter consolidation, RDS right-sizing.',
     'Typical work: Karpenter consolidation, RDS right-sizing, commitment and storage reviews.'),
    ('incident processes that cut MTTR', 'incident processes that hold up at 3 a.m.'),
    ('Fixed-scope work, production outcomes.', 'Fixed-scope work, honestly scoped.'),
    ('at 8–10 crore monthly users', 'at national scale'),
    ('full parity, zero data loss — and come out the other side faster than before', 'full parity — verified endpoint by endpoint before cutover'),
    ('MTTR 90 → &lt;20 min.', 'observability and runbook standardisation.'),
]


FINAL_FIXES = [
    ('Performance-tuned in production: note structuring went from ~115 seconds to ~5 seconds (warm model, tuned inference); a 33-second dictation is review-ready in about a minute on CPU alone.',
     'Performance work centred on the inference path: keeping the model warm, trimming decoding parameters and parallelising transcription, until dictation felt like a tool rather than a wait.'),
    ('Proved as an isolated POC alongside the live system — zero downtime, live data untouched — passing validation across EMR, OPD, Pathology, Radiology, Pharmacy, Billing, IPD and Discharge with 100% field accuracy on Hinglish dictation .',
     'Proved as an isolated POC alongside the live system — live data untouched — and validated module-by-module across EMR, OPD, Pathology, Radiology, Pharmacy, Billing, IPD and Discharge on Hinglish dictation.'),
    ('Sustained 99.95% availability across two release trains with zero Sev-1 incidents on a hybrid EKS + ECS estate, multi-AZ Envoy ingress, KEDA-driven autoscaling, and SLO / error-budget release gates.',
     'Run the hybrid EKS + ECS estate behind multi-AZ Envoy ingress, with KEDA-driven autoscaling and releases gated on SLOs and error budgets rather than calendar dates.'),
    ('Delivered a zero-downtime migration — zero customer-impacting minutes, 99.9% post-migration SLO — via active-active EKS with Route 53 weighted traffic shifts and Terraform-managed landing zones.',
     'Executed the migration as an active-active EKS move with Route 53 weighted traffic shifts and Terraform-managed landing zones — traffic moved in measured, reversible steps.'),
    ('Cut infrastructure cost by 30% while doubling traffic capacity : replaced manual provisioning with reusable Terraform modules, Karpenter-driven node consolidation, and right-sized RDS PostgreSQL tiers.',
     'Replaced manual provisioning with reusable Terraform modules, Karpenter-driven node consolidation and right-sized RDS PostgreSQL tiers — cost treated as an architectural input, reviewed at every release.'),
    ('Closed the Azure → GCP migration ahead of deadline with zero data loss and 100% endpoint parity : workloads re-platformed on GKE , pipelines rebuilt on Cloud Build , and keyless service auth via Workload Identity .',
     'Re-platformed the workloads onto GKE, pipelines rebuilt on Cloud Build, and keyless service auth via Workload Identity — endpoint parity verified service-by-service before cutover.'),
]

def scrub(html):
    html = drop_block(html, 'class="metric-row"')
    for a, b in PHRASE_FIXES:
        html = html.replace(a, b)
    for a, b in FLEX_FIXES:
        html = flex(html, a, b)
    for a, b in FINAL_FIXES:
        html = flex(html, a, b)
    html = html.replace('up to 100M MAU', 'citizen scale')
    html = html.replace('p95 latency −35%', 'per-route traffic policy')
    html = html.replace('Sixty seconds later a structured clinical note is on screen for her confirmation.',
                        'The structured clinical note appears on screen for her confirmation.')
    html = html.replace('structured note · ~5s', 'structured note')
    html = html.replace('structured note · ~5 s', 'structured note')
    return html

# ---------------- Case pages ----------------
def case_body(n):
    c = next(x for x in cases if x['n'] == n)
    html = c['html']
    html = re.sub(r'<div class="case-index">.*?</div>', '', html, flags=re.S)
    html = re.sub(r'<h3>.*?</h3>', '', html, count=1, flags=re.S)
    html = html.replace('src="hms-voice-ai-architecture.png"',
                        f'src="{BASE}assets/hms-voice-ai-architecture.webp" loading="lazy"')
    html = scrub(html)
    if n in EXTRAS:
        html = html.replace('</article>', EXTRAS[n] + '</article>')
    slug, tag = SLUGS[n]
    order = [x['n'] for x in cases]
    i = order.index(n)
    prev_n = order[i - 1] if i > 0 else None
    next_n = order[i + 1] if i < len(order) - 1 else None
    nav = '<nav class="case-nav" aria-label="More case studies">'
    if prev_n:
        pc = next(x for x in cases if x['n'] == prev_n)
        nav += f'<a href="{BASE}work/{SLUGS[prev_n][0]}/">← {pc["title"]}</a>'
    nav += f'<a href="{BASE}work/">All case studies</a>'
    if next_n:
        nc = next(x for x in cases if x['n'] == next_n)
        nav += f'<a href="{BASE}work/{SLUGS[next_n][0]}/">{nc["title"]} →</a>'
    nav += '</nav>'
    return f'''
      <section class="cases casepage"><div class="wrap">
        <p class="crumb mono"><a href="{BASE}">Home</a> · <a href="{BASE}work/">Work</a> · CASE {n}</p>
        <h1 class="case-h1">{c['title']}</h1>
        <p class="case-tag mono">{tag}</p>
        {html}
        {nav}
      </div></section>'''

for c in cases:
    n = c['n']; slug, tag = SLUGS[n]
    desc = ONELINERS[n]
    write(f'work/{slug}/index.html', page(f'{c["title"]} — Case Study | Shahrukh Khan', desc, f'work/{slug}/', case_body(n)))

# ---------------- Work index ----------------
def work_index():
    cards = ''
    for c in cases:
        n = c['n']; slug, tag = SLUGS[n]
        cards += f'''
            <a class="flag-card reveal" href="{BASE}work/{slug}/">
              <div class="f-tag mono">CASE {n} · {tag}</div>
              <h3>{c['title']}</h3>
              <p>{ONELINERS[n]}</p>
              <span class="f-link">Read the case study →</span>
            </a>'''
    return f'''
      <section class="flag-sec" style="padding-top: clamp(48px,6vw,84px)"><div class="wrap">
        <div class="section-head reveal">
          <span class="kicker no-bar mono" style="display:block;margin-bottom:6px;color:var(--accent);letter-spacing:0.12em;">WORK</span>
          <h2>Nine engagements, documented as executed.</h2>
          <p class="lede">Each case study follows the same discipline: the brief, the constraints, the architecture, what was actually done — and for the flagship three, the decisions, their alternatives, and the lessons.</p>
        </div>
        <div class="flag-grid">{cards}</div>
      </div></section>'''
write('work/index.html', page('Case Studies — Shahrukh Khan', 'Nine platform engagements documented as executed: national government platforms, regulated fintech migrations, production MLOps, a self-hosted AI agent platform and hospital voice AI.', 'work/', work_index()))

# ---------------- Consulting ----------------
def consulting_body():
    return f'''
      <section class="flag-sec" style="padding-top: clamp(48px,6vw,84px)"><div class="wrap">
        <div class="section-head reveal">
          <span class="kicker no-bar mono" style="display:block;margin-bottom:6px;color:var(--accent);letter-spacing:0.12em;">CONSULTING — SARVNEX TECHNOLOGIES</span>
          <h2>Platform problems, solved as engagements.</h2>
          <p class="lede">Consulting runs through Sarvnex Technologies, alongside a full-time platform role. That constraint is a feature: scope is agreed in writing before work begins, and every engagement is executed with the same gates I run in production.</p>
        </div>
        <div class="approach-grid">
          <div class="approach-card reveal"><div class="a-num">A</div><h3>Reliability &amp; platform audits</h3><p>A structured review of your cloud estate — architecture, release process, observability, security posture — delivered as a findings report with a prioritised, costed remediation plan. You keep the report either way.</p></div>
          <div class="approach-card reveal" data-delay="1"><div class="a-num">B</div><h3>Cloud builds &amp; migrations</h3><p>Landing zones, Kubernetes platforms and zero-downtime migrations executed build-before-teardown, with named rollbacks and parity checks at every step — the method behind the fintech and re-platforming case studies.</p></div>
          <div class="approach-card reveal" data-delay="2"><div class="a-num">C</div><h3>AI deployment &amp; agents</h3><p>Self-hosted LLM platforms, voice AI and agent systems where data residency rules out public APIs — designed, proven as an isolated POC first, then integrated behind confirmation gates.</p></div>
          <div class="approach-card reveal" data-delay="3"><div class="a-num">D</div><h3>Cost &amp; FinOps reviews</h3><p>Where the cloud bill actually goes, and the engineering changes that reduce it — rightsizing, consolidation and architecture-level fixes, reported against your own billing data.</p></div>
        </div>
        <div class="hld reveal" style="margin-top:34px"><span class="kicker no-bar mono" style="font-size:11.5px;color:var(--accent);letter-spacing:0.14em;">HOW AN ENGAGEMENT RUNS</span>
          <div class="hld-notes">
            <div class="hld-note"><strong>1 · Assess</strong>A short discovery call and read-only review. You get an honest read on the problem — including if the answer is "don't build this".</div>
            <div class="hld-note"><strong>2 · Agree</strong>Fixed scope, deliverables and price in writing. No open-ended day rates, no surprise line items.</div>
            <div class="hld-note"><strong>3 · Execute</strong>Work proceeds in verified steps with rollbacks named in advance; you see evidence at each step, not status theatre.</div>
            <div class="hld-note"><strong>4 · Hand over</strong>Runbooks, diagrams and decisions documented so your team can operate it without me. The engagement ends; the operability stays.</div>
          </div></div>
        <div class="teaser-card reveal" style="margin-top:34px">
          <div><h2 style="margin:0 0 8px">Start with the problem, not a purchase order.</h2>
          <p style="margin:0">Write to <a href="mailto:hello@sarvnex.com">hello@sarvnex.com</a> with what is breaking, slow, expensive or unshipped. You will get a direct reply — and an honest first read before any proposal.</p></div>
          <a class="btn btn-primary" href="mailto:hello@sarvnex.com?subject=Consulting%20inquiry%20via%20portfolio">Email Sarvnex <span class="arr">→</span></a>
        </div>
      </div></section>'''
write('consulting/index.html', page('Consulting — Sarvnex Technologies | Shahrukh Khan', 'Fixed-scope consulting through Sarvnex Technologies: reliability audits, cloud builds and migrations, self-hosted AI deployment, and FinOps reviews. Assessed first, quoted in writing, handed over operable.', 'consulting/', consulting_body()))

# ---------------- 404, sitemap, robots ----------------
write('404.html', page('Page not found — Shahrukh Khan', 'That page does not exist.', '404.html', f'''
      <section class="flag-sec" style="padding-top: clamp(64px,8vw,110px)"><div class="wrap">
        <div class="section-head">
          <span class="kicker no-bar mono" style="display:block;margin-bottom:6px;color:var(--accent);letter-spacing:0.12em;">404</span>
          <h2>This route doesn't resolve.</h2>
          <p class="lede">The page you asked for isn't here. The atlas is: <a href="{BASE}">home</a>, <a href="{BASE}work/">case studies</a>, <a href="{BASE}consulting/">consulting</a>.</p>
        </div>
      </div></section>'''))
urls = ['', 'work/'] + [f'work/{SLUGS[c["n"]][0]}/' for c in cases] + ['consulting/']
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for u in urls:
    sm += f'  <url><loc>https://khanblogs.github.io{BASE}{u}</loc><lastmod>2026-11-26</lastmod></url>\n'
sm += '</urlset>\n'
write('sitemap.xml', sm)
write('robots.txt', f'User-agent: *\nAllow: /\nSitemap: https://khanblogs.github.io{BASE}sitemap.xml\n')
print('ALL PAGES GENERATED')

write('index.html', page(
    'Shahrukh Khan — Cloud & AI Platform Engineer',
    'Cloud & AI Platform Engineer. Kubernetes, MLOps and self-hosted AI platforms for national-scale government platforms, regulated fintech and startups. Method: prove in isolation, gate on evidence, zero-downtime execution.',
    '', home_body(), PERSON_LD))
print('HOME WRITTEN LAST')
