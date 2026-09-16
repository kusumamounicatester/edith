# EDITH — Developer Handoff

Two separate deliverables, deliberately not one codebase:

```
edith-homepage/     → the public marketing site. Vanilla HTML/CSS/JS, no build step,
                       no login. Deploy anywhere that serves static files.
edith-admin-crm/     → the ONE login in the whole platform. Node/Express/MongoDB.
                       Deploy to its own domain/subdomain with a real Node runtime.
```

They're separate on purpose: 20 marketing pages need zero backend, and bolting one on
"just in case" adds cost and failure points for no benefit. The one thing that
genuinely needs a server — the admin lead dashboard — gets one, same split already
running on Gooz.ai (static frontend + `crm.gooz.ai` as a separate Node app).

## edith-homepage/ — what's built

All 20 pages from brief §4's sitemap, sharing one header/nav/footer and one design
system (`css/tokens.css`, `css/global.css`, `css/pages.css`, `css/homepage.css`):

| Page | Brief section |
|---|---|
| `index.html` | Homepage, §5 |
| `invest-with-us.html` | §6.1 |
| `builder-jv.html` (+ working JV Sharing Calculator) | §6.2 |
| `professional-services.html` | §6.3 |
| `get-a-quote.html` (+ multi-step quote wizard) | §6.4 |
| `internships.html` | §6.5 |
| `engineer-partnership.html` | §6.6 |
| `training-placement.html` | §6.7 |
| `property-marketplace.html` + `become-an-agent.html` | §6.8 |
| `blog/index.html` + `calculators.html` | §6.9, §8 |
| `about.html`, `contact.html`, `careers.html`, `faqs.html` | §4 standalone links |
| `privacy-policy.html`, `terms.html`, `disclaimer.html`, `refund-policy.html`, `sitemap.html` | §16 legal footer |

### How pages are generated (read this before hand-editing any page)

Every page except `index.html` is generated from `_build/pages_content.py` by
`_build/generate_pages.py`, which stitches each page's content into the exact same
header/nav/footer pulled live from `index.html`. **If you need to change the header,
footer, or nav — edit `index.html`, then re-run the generator:**

```bash
cd edith-homepage
python3 _build/generate_pages.py
```

This is a dev-only build step — the *output* is 20 plain, standalone `.html` files with
no includes and no runtime dependency on the script. Once generated, you can hand-edit
any single page directly if a change is truly page-specific; just know it'll be
overwritten if someone re-runs the generator later without also updating
`pages_content.py`.

### Forms → CRM wiring

Every form with a `data-module="..."` attribute is intercepted by `js/lead-forms.js`
and POSTed as JSON to `edith-admin-crm`'s `/api/leads` endpoint, tagged with module,
source, timestamp, and (if the homepage router was used) visitor type — this is brief
§10's "one shared CRM" requirement, already wired end to end. **Before go-live**, open
`js/lead-forms.js` and replace:

```js
var EDITH_API_BASE = 'https://crm.edith.example/api'; // [PLACEHOLDER]
```

with wherever `edith-admin-crm` actually gets deployed.

### Calculators (brief §8 — 10 total)

- **Live and working:** Construction cost estimator (`js/calculator.js`), Land-unit
  converter (`js/land-converter.js`), JV Sharing Calculator (`js/jv-calculator.js`).
- **Listed, not yet built:** the other seven on `calculators.html` — home-loan EMI,
  stamp duty, GST, JDA share, ROI, rental yield, plot-vs-flat, feasibility. Each needs
  EDITH-confirmed rates before it's worth building (see next section) — they follow the
  exact same pattern as the three that exist.

### Every [PLACEHOLDER] — the §17 checklist

Search any file for `[PLACEHOLDER` to find every spot needing a real client input:
CIN/RERA/GST numbers, real project/hero photos (brief explicitly bans stock photography),
track-record stats, testimonial quotes, blog posts, WhatsApp number, calculator
rate tables, and every legal page (all four are lawyer-review stubs, per brief §16).

## edith-admin-crm/ — what's built

See `edith-admin-crm/README.md` for full setup. In short: one admin login, one
dashboard showing every lead from all 9 modules with filtering and a pipeline-stage
dropdown, and the public `/api/leads` endpoint every form on the marketing site posts to.

## What's deliberately still open

- **Real i18n** (§9): `#langToggle` on every page is a stub that toggles a body class.
  Actual English/Telugu/Tenglish content switching needs a translation workflow and
  real Telugu copy — not built here.
- **Blog CMS**: `blog/index.html` has placeholder posts. Brief §17 calls for 8–10
  starter posts repurposed from EDITH's existing Reels — needs an actual CMS or
  hand-authored posts once that content exists.
- **File uploads** (resumes, listing photos): forms collect a filename only; no storage
  backend (S3/Cloudinary/etc.) is wired up.
- **Legal pages**: all four are explicitly marked "not yet lawyer-reviewed" per brief
  §16 — don't let these go live as-is.
- **Property listing moderation queue**: brief §11 calls for an admin moderation step
  before listings go live. The admin CRM here only handles lead-pipeline stages; a
  separate `Listing` model + moderation UI would extend the same backend.
