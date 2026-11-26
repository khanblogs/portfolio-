# Résumé extraction test — 2026-11-26
Files: assets/Shahrukh_Khan_Resume.pdf (2 pages, fpdf2, embedded DejaVu) + .docx (python-docx). Single column, no tables, no text boxes, no graphics.
Method: pdftotext -layout on the PDF; paragraph dump on the DOCX.
Results (actual):
- Reading order correct in both: name → title → contact → summary → skills → experience (reverse chronological) → education → certifications → languages.
- Contact details extract intact: +91-9811731300, iamdevopskhan@gmail.com, linkedin.com/in/shahrukhkhan-devops.
- Dates extract as text (e.g. "Nov 2025 - Present"); IIT Guwahati entry reads "Completed September 2026" (owner-updated fact).
- Skill terms present as plain text: Kubernetes, Terraform, EKS, Argo CD, OpenTelemetry, Kubeflow, MLflow, Istio, Karpenter.
- Per owner direction (2026-11-26), result-metric claims were omitted from the résumé as well; bullets describe scope, method and responsibility. No ATS score is claimed — no universal score exists.
