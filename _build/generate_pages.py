#!/usr/bin/env python3
"""
Dev-only build helper — NOT part of the site itself, and not something the
client needs to run. It exists purely so every page shares one exact copy of
the header/nav/footer instead of nine hand-retyped, slowly-drifting copies.

Run once from /home/claude/edith-homepage:  python3 _build/generate_pages.py
Output: finished, standalone .html files at the project root — each one
works on its own with zero includes/build-step once generated.
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(ROOT, "index.html"), encoding="utf-8") as f:
    home = f.read()

HEADER = home[home.index('<a href="#main" class="skip-link">'): home.index('<main id="main">')]
FOOTER = home[home.index("</main>") + len("</main>"): home.index("<script>document.getElementById('yearNow')")]

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<script type="application/ld+json">
{schema}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}css/tokens.css">
<link rel="stylesheet" href="{prefix}css/global.css">
<link rel="stylesheet" href="{prefix}css/pages.css">
</head>
<body>
{header}
<main id="main">
{body}
</main>
{footer}
<script>document.getElementById('yearNow').textContent = new Date().getFullYear();</script>
<script src="{prefix}js/i18n-te.js"></script>
<script src="{prefix}js/global.js"></script>
<script src="{prefix}js/lead-forms.js"></script>
{extra_scripts}
</body>
</html>
"""

HREF_RE = re.compile(r'href="([^"]+)"')

def prefix_relative_links(html, prefix):
    """Rewrite relative internal hrefs (page.html, blog/index.html, page.html#anchor)
    so they still resolve correctly from a subdirectory. Leaves anchors-only,
    external links (http/https), and mailto/tel untouched."""
    if not prefix:
        return html
    def sub(m):
        href = m.group(1)
        if href.startswith(("#", "http://", "https://", "mailto:", "tel:", "javascript:", prefix)):
            return m.group(0)
        return 'href="%s%s"' % (prefix, href)
    return HREF_RE.sub(sub, html)

def write_page(filename, title, description, body, schema='{"@context":"https://schema.org","@type":"WebPage"}', extra_scripts="", prefix=""):
    header = prefix_relative_links(HEADER, prefix)
    footer = prefix_relative_links(FOOTER, prefix)
    out = PAGE_TEMPLATE.format(
        title=title, description=description, schema=schema,
        header=header, body=body, footer=footer,
        extra_scripts=extra_scripts, prefix=prefix
    )
    path = os.path.join(ROOT, filename)
    os.makedirs(os.path.dirname(path), exist_ok=True) if os.path.dirname(path) else None
    with open(path, "w", encoding="utf-8") as f:
        f.write(out)
    print("wrote", filename, len(out), "bytes")

if __name__ == "__main__":
    from pages_content import PAGES
    for filename, spec in PAGES.items():
        write_page(filename, **spec)
