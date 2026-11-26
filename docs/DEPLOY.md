# Deployment & rollback — portfolio v2 (2026-11-26)
Source of truth: this repository (khanblogs/portfolio-). The site is fully static; build/ contains the generator (gen.py, resume.py, src/) that produced the pages from the v1 content with the claim-scrub rules encoded.
Publish: commit on main → push → checkout gh-pages → merge main → push. GitHub Pages serves /portfolio-/.
Verify after publish: /, /work/, /work/hms-voice-ai/, /consulting/, /assets/Shahrukh_Khan_Resume.pdf, /sitemap.xml, /robots.txt all return 200; spot-check one case page visually.
Rollback: revert gh-pages to the pre-v2 commit (the v1 one-pager, commit fd6bf0e line) — `git checkout gh-pages && git revert --no-commit <v2-merge> .. ` or reset to fd6bf0e-era gh-pages head and force-push with owner's approval. The v1 single file remains complete and self-contained.
