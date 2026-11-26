# -*- coding: utf-8 -*-
"""ATS résumé — single column, selectable text, no tables/graphics. Facts from owner's CV; result-claims omitted per owner direction."""
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os

OUT = '/home/hatch/workspace/portfolio-v2/assets'
NAME = 'Shahrukh Khan'
TITLE = 'Senior DevOps Engineer | MLOps Engineer | Platform Engineer'
CONTACT = 'New Delhi, India | +91-9811731300 | iamdevopskhan@gmail.com | linkedin.com/in/shahrukhkhan-devops | github.com/khanblogs | khanblogs.github.io/portfolio-'
SUMMARY = ('Senior DevOps Engineer at Digital India Corporation, NeGD (MeitY, Govt. of India), where I lead the AWS '
           'platform behind UMANG, the national super-app for citizen services, and deliver DevOps for NITI Aayog '
           'programmes (UPMS, NITI For States, NGO Darpan). Eight years across government platforms, regulated '
           'fintech, startups and international consulting. Working method: prove new systems in isolation, gate '
           'releases on SLOs and error budgets, build before teardown, and hand over platforms other engineers can '
           'operate. Deep practice across Kubernetes, Terraform, GitOps, service mesh, DevSecOps, MLOps and '
           'self-hosted AI platforms.')
SKILLS = [
    ('Cloud', 'AWS, Microsoft Azure, Google Cloud, NIC Meghraj (Govt. of India National Cloud), DigitalOcean'),
    ('Containers & Orchestration', 'Docker, Kubernetes (EKS, ECS, GKE, AKS), Helm, Karpenter, Istio service mesh, Envoy'),
    ('IaC & GitOps', 'Terraform, Crossplane, Ansible, CloudFormation, Argo CD, Argo Rollouts'),
    ('CI/CD', 'GitHub Actions, GitLab CI/CD, Jenkins, AWS CodePipeline, OIDC keyless authentication'),
    ('Observability & SRE', 'SLO/SLI and error budgets, Prometheus, Grafana, OpenTelemetry, ELK Stack, Datadog, New Relic'),
    ('Security & DevSecOps', 'OPA/Gatekeeper, Cosign/Sigstore, SBOM (Syft), Trivy, IAM, IRSA, RBAC, WAF, GuardDuty, secrets management'),
    ('MLOps & AI', 'Kubeflow, MLflow, Airflow, FastAPI, vector databases, self-hosted LLM platforms, AI agents'),
    ('Data', 'PostgreSQL, MySQL, MongoDB, Redis'),
    ('Languages', 'Python, Bash/Shell, Go, Linux administration'),
]
ROLES = [
    ('Senior DevOps Engineer', 'Digital India Corporation, NeGD (MeitY, Govt. of India)', 'New Delhi, India', 'Nov 2025 - Present', [
        'Own the AWS platform behind UMANG: hybrid EKS + ECS estate, multi-AZ Envoy ingress, KEDA-driven autoscaling, and releases gated on SLOs and error budgets.',
        'Lead DevOps and platform delivery for NITI Aayog flagship programmes (UPMS, NITI For States, NGO Darpan): HLD/LLD architecture, AWS infrastructure, CI/CD pipelines and production deployments.',
        'Led the integration of MyScheme into the UMANG app: environment parity, secure VPC peering, CI/CD wiring and production cutover.',
        'Standardised OpenTelemetry instrumentation and shared SRE runbooks across the microservice estate, including integrations with EPFO, DigiYatra, DigiLocker and NSSO.']),
    ('Lead DevOps and MLOps Engineer', 'Creditech Solutions (AlphaMoney, fintech)', 'Gurugram, India', 'Feb 2024 - Aug 2025', [
        'Executed a zero-downtime AWS migration for a regulated fintech workload as an active-active EKS move with Route 53 weighted traffic shifts and Terraform-managed landing zones.',
        'Replaced manual provisioning with reusable Terraform modules, Karpenter-driven node consolidation and right-sized RDS PostgreSQL tiers.',
        'Built the platform for a production Bank Statement Analyzer for credit decisioning: FastAPI inference, Airflow ETL/feature pipelines, MLflow registry, Kubernetes autoscaling.',
        'Extended platform and DevOps practices across parent-group ventures (AlphaCorp, Alpha Design Studio), including cloud-hosted ERP and a secure corporate intranet.']),
    ('DevOps and Cloud Architect', 'Trezi (Smartvizx)', 'Noida, India', 'Jul 2023 - Jan 2024', [
        'Re-platformed workloads from Azure to GCP on GKE with Cloud Build pipelines and Workload Identity for keyless auth; endpoint parity verified service-by-service before cutover.',
        'Introduced an Istio service mesh for traffic shaping, mTLS and per-route retry/timeout policies.']),
    ('DevOps Engineer', 'Bada Business Pvt. Ltd.', 'New Delhi, India', 'Mar 2023 - Jul 2023', [
        'Ran an AWS to GCP migration for a high-traffic edtech platform: containerized workloads re-platformed with Terraform-managed infrastructure and automated CI/CD cutover.']),
    ('DevOps Engineer', 'SignCatch (SKY Inno Labs)', 'New Delhi, India', 'Nov 2021 - Jul 2022', [
        'Migrated a Docker-based microservices estate from AWS to Azure AKS with Azure DevOps CI/CD and ELK + Azure Monitor observability.',
        'Standardized Docker base images, Helm chart templates and a shared CI pipeline reused across the microservices estate.']),
    ('Project Engineer', 'Samarth eGov (University of Delhi)', 'New Delhi, India', 'Aug 2020 - Oct 2021', [
        'Automated Linux provisioning, backup and routine operations for the eGov Samarth ERP rollout with Bash and Python scripting and UiPath-orchestrated workflows.']),
    ('IT Administrator', 'Deep Public School', 'New Delhi, India', 'Feb 2019 - Aug 2020', [
        'Owned end-to-end IT operations: on-premise servers, ERP, school domain/email and digital presence.']),
    ('Advisory and Consulting Engagements', 'Cloud, DevOps and MLOps (alongside primary roles)', 'India / Remote', '2023 - 2025', [
        'Aftershoot (AI startup): cloud cost, GPU workload orchestration and CI/CD for AI/ML pipelines.',
        'ZS Associates: real-time and batch inference HLD/LLD for a pharma-analytics MLOps platform on Kubeflow + MLflow.',
        'Servando Technologies (Boston): Terraform + GitHub Actions reference HLD/LLD adopted as a team baseline.',
        'Enterprise Monkey: stabilized a Drupal estate on AWS + Acquia.']),
]
EDUCATION = [
    'MSc in Data Science | Symbiosis International University | 2025 - Present',
    'Minor Degree in Data Science | IIT Guwahati | Completed September 2026',
    'PGDIT | Symbiosis Centre for Distance Learning | 2020 - 2022',
    'Bachelor of Arts | University of Delhi | 2016 - 2019',
]
CERTS = ('AWS Certified DevOps Engineer - Professional; AWS Certified Solutions Architect - Professional; '
         'Generative AI with Large Language Models (DeepLearning.AI); Cybersecurity and Data Science (Cisco); '
         'Project Management Essentials Certified')
LANGS = 'English, Hindi, Urdu'

# ---------- DOCX ----------
doc = Document()
for s in doc.sections:
    s.top_margin = Inches(0.6); s.bottom_margin = Inches(0.6); s.left_margin = Inches(0.7); s.right_margin = Inches(0.7)
st = doc.styles['Normal']; st.font.name = 'Calibri'; st.font.size = Pt(10.5)
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run(NAME); r.bold = True; r.font.size = Pt(20)
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run(TITLE); r.bold = True; r.font.size = Pt(11.5)
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.add_run(CONTACT).font.size = Pt(9.5)

def h2(text):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(12); p.paragraph_format.space_after = Pt(4)
    r = p.add_run(text); r.bold = True; r.font.size = Pt(12.5)
    return p

h2('PROFESSIONAL SUMMARY'); doc.add_paragraph(SUMMARY)
h2('TECHNICAL SKILLS')
for k, v in SKILLS:
    p = doc.add_paragraph(); r = p.add_run(k + ': '); r.bold = True; p.add_run(v)
h2('PROFESSIONAL EXPERIENCE')
for role, org, loc, dates, bullets in ROLES:
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(8)
    r = p.add_run(f'{role} | {org}'); r.bold = True
    p = doc.add_paragraph(); p.add_run(f'{loc} | {dates}').italic = True
    for b in bullets:
        doc.add_paragraph(b, style='List Bullet')
h2('EDUCATION')
for e in EDUCATION:
    doc.add_paragraph(e, style='List Bullet')
h2('CERTIFICATIONS'); doc.add_paragraph(CERTS)
h2('LANGUAGES'); doc.add_paragraph(LANGS)
doc.save(f'{OUT}/Shahrukh_Khan_Resume.docx')
print('DOCX written')

# ---------- PDF (fpdf2, selectable text) ----------
from fpdf import FPDF
F = '/usr/share/fonts/truetype/dejavu/'
class R(FPDF):
    pass
pdf = R('P', 'mm', 'A4'); pdf.set_auto_page_break(True, 16)
pdf.add_font('D', '', F + 'DejaVuSans.ttf'); pdf.add_font('D', 'B', F + 'DejaVuSans-Bold.ttf'); pdf.add_font('D', 'I', F + 'DejaVuSansMono-BoldOblique.ttf')
pdf.add_page(); pdf.set_margins(16, 14, 16); pdf.set_y(14)
def center(txt, size, bold=False, gap=5):
    pdf.set_font('D', 'B' if bold else '', size); pdf.cell(0, gap, txt, align='C', new_x='LMARGIN', new_y='NEXT')
def h2p(txt):
    pdf.ln(4); pdf.set_font('D', 'B', 12); pdf.cell(0, 6, txt, new_x='LMARGIN', new_y='NEXT')
    pdf.set_draw_color(160); pdf.line(16, pdf.get_y(), 194, pdf.get_y()); pdf.ln(2)
def para(txt, size=9.8):
    pdf.set_font('D', '', size); pdf.multi_cell(0, 4.8, txt, new_x='LMARGIN', new_y='NEXT')
def bullet(txt):
    pdf.set_font('D', '', 9.8); pdf.cell(5); pdf.multi_cell(0, 4.8, '• ' + txt, new_x='LMARGIN', new_y='NEXT')
center(NAME, 19, True, 8); center(TITLE, 11, True, 6)
center('New Delhi, India | +91-9811731300 | iamdevopskhan@gmail.com', 8.6, False, 4.6)
center('linkedin.com/in/shahrukhkhan-devops | github.com/khanblogs | khanblogs.github.io/portfolio-', 8.6, False, 5)
h2p('PROFESSIONAL SUMMARY'); para(SUMMARY)
h2p('TECHNICAL SKILLS')
for k, v in SKILLS:
    pdf.set_font('D', '', 9.8); pdf.multi_cell(0, 4.8, k + ': ' + v, new_x='LMARGIN', new_y='NEXT')
h2p('PROFESSIONAL EXPERIENCE')
for role, org, loc, dates, bullets in ROLES:
    pdf.ln(2); pdf.set_font('D', 'B', 10.4); pdf.multi_cell(0, 5, f'{role} | {org}', new_x='LMARGIN', new_y='NEXT')
    pdf.set_font('D', 'I', 9.4); pdf.cell(0, 4.6, f'{loc} | {dates}', new_x='LMARGIN', new_y='NEXT')
    for b in bullets: bullet(b)
h2p('EDUCATION')
for e in EDUCATION: bullet(e)
h2p('CERTIFICATIONS'); para(CERTS)
h2p('LANGUAGES'); para(LANGS)
pdf.output(f'{OUT}/Shahrukh_Khan_Resume.pdf')
print('PDF written')
