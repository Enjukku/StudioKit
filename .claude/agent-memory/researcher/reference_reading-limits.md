---
name: reading-limits-for-pdf-sources
description: Which source types the researcher's tools can and cannot read (PDF text layers, arXiv, paywalls, no Bash); saves retries on statistics and paper fact-checks
metadata:
  type: reference
---

Learned in J013-T02 (2026-10-21).

- WebFetch cannot read PDFs whose text is Flate-compressed (Kohavi 2009 survey, ASA p-value statement, Lehr 1992, arXiv PDFs): it returns "unreadable". Do not retry on other hosts of the same PDF.
- For arXiv papers use `https://ar5iv.labs.arxiv.org/html/<id>`: full readable text (worked for 1506.00356, 1803.06336, 1512.04922, 1602.05549, 2305.16459). Use the `/abs/` page for title, authors, date.
- Springer (cookie redirect), tandfonline and researchgate return 403 or a login redirect. PMC (`pmc.ncbi.nlm.nih.gov/articles/PMC...`) works.
- Microsoft ExP articles, Microsoft Learn (PlayFab page shows `updated_at` in its metadata), Wikipedia, NIST handbook pages, statsmodels source on raw.githubusercontent.com all read fine.
- The researcher has no Bash tool: check values must be computed by hand. Show the arithmetic and give a tolerance.
- When a primary text cannot be read, say so in "How I checked", mark the row unverified-kept-with-label, and keep the math as an independent check.
