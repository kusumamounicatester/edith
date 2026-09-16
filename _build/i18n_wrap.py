#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
One-time instrumentation pass: wraps translatable text nodes in <span
data-i18n="tNNNN"> and tags translatable attributes with companion
data-i18n-attr-<name>="tNNNN" attributes, across index.html (header/footer/
homepage body) and every page body inside _build/pages_content.py.

Run once: python3 _build/i18n_wrap.py
Outputs: rewrites index.html + pages_content.py in place, and writes
_build/i18n_strings.json — the manifest of unique English strings needing
Telugu translation (key -> English text).
"""
import re, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STRINGS = {}          # key -> english text
TEXT_TO_KEY = {}       # english text -> key (dedup)
_counter = [0]

TRANSLATABLE_ATTRS = ("placeholder", "aria-label", "alt", "title")

LETTER_RE = re.compile(r"[A-Za-z]{2,}")
TAG_RE = re.compile(r"<[^>]+>", re.DOTALL)
COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
OPAQUE_BLOCK_RE = re.compile(r"<(script|style|textarea)\b.*?</\1>", re.DOTALL | re.IGNORECASE)


def get_key(text):
    norm = text.strip()
    if norm in TEXT_TO_KEY:
        return TEXT_TO_KEY[norm]
    _counter[0] += 1
    key = "t%04d" % _counter[0]
    TEXT_TO_KEY[norm] = key
    STRINGS[key] = norm
    return key


def wrap_attrs_in_tag(tag_text):
    """Given a raw '<tag ...>' string, add data-i18n-attr-<name> for any
    translatable attribute that has real text content."""
    if not tag_text.startswith("<") or tag_text.startswith("</"):
        return tag_text
    new_attrs = []
    def attr_sub(m):
        name, val = m.group(1), m.group(2)
        if LETTER_RE.search(val) and "{" not in val:  # skip template-y values
            key = get_key(val)
            new_attrs.append(' data-i18n-attr-%s="%s"' % (name, key))
        return m.group(0)
    attr_pattern = re.compile(r'\b(%s)="([^"]*)"' % "|".join(TRANSLATABLE_ATTRS))
    tag_text = attr_pattern.sub(attr_sub, tag_text)
    if new_attrs:
        tag_text = tag_text[:-1].rstrip() + "".join(new_attrs) + tag_text[-1:]
    return tag_text


def wrap_html_text(html):
    """Wrap qualifying visible text runs in <span data-i18n="key">, and tag
    translatable attributes. Leaves scripts/styles/comments untouched."""
    if "<" not in html:
        return html

    out = []
    pos = 0
    # First carve out opaque blocks (script/style) and comments so we never
    # touch their insides; everything else goes through tag/text tokenizing.
    protect_re = re.compile(
        r"(<(?:script|style|textarea)\b.*?</(?:script|style|textarea)>)|(<!--.*?-->)",
        re.DOTALL | re.IGNORECASE,
    )
    last = 0
    segments = []  # (is_protected, text)
    for m in protect_re.finditer(html):
        if m.start() > last:
            segments.append((False, html[last:m.start()]))
        segments.append((True, m.group(0)))
        last = m.end()
    if last < len(html):
        segments.append((False, html[last:]))

    for is_protected, seg in segments:
        if is_protected:
            out.append(seg)
            continue
        # tokenize this segment into tags and text
        idx = 0
        for tm in TAG_RE.finditer(seg):
            text = seg[idx:tm.start()]
            if text:
                out.append(_wrap_text_run(text))
            tag = tm.group(0)
            out.append(wrap_attrs_in_tag(tag))
            idx = tm.end()
        if idx < len(seg):
            out.append(_wrap_text_run(seg[idx:]))
    return "".join(out)


def _wrap_text_run(text):
    if not LETTER_RE.search(text):
        return text
    stripped = text.strip()
    if not stripped:
        return text
    lead_len = len(text) - len(text.lstrip())
    trail_len = len(text) - len(text.rstrip())
    lead = text[:lead_len]
    trail = text[len(text) - trail_len:] if trail_len else ""
    key = get_key(stripped)
    return '%s<span data-i18n="%s">%s</span>%s' % (lead, key, stripped, trail)


def process_index_html():
    path = os.path.join(ROOT, "index.html")
    with open(path, encoding="utf-8") as f:
        home = f.read()

    header_start = home.index('<a href="#main" class="skip-link">')
    main_start = home.index("<main id=\"main\">")
    main_end = home.index("</main>") + len("</main>")
    footer_end = home.index("<script>document.getElementById('yearNow')")

    header = home[header_start:main_start]
    body = home[main_start:main_end]
    footer = home[main_end:footer_end]

    header_w = wrap_html_text(header)
    body_w = wrap_html_text(body)
    footer_w = wrap_html_text(footer)

    new_home = home[:header_start] + header_w + body_w + footer_w + home[footer_end:]
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_home)
    print("index.html instrumented:", len(new_home), "bytes")


def process_pages_content():
    path = os.path.join(ROOT, "_build", "pages_content.py")
    with open(path, encoding="utf-8") as f:
        src = f.read()

    parts = src.split('"""')
    for i in range(1, len(parts), 2):  # odd indices = inside triple-quotes
        if "<" in parts[i]:
            parts[i] = wrap_html_text(parts[i])
    new_src = '"""'.join(parts)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_src)
    print("pages_content.py instrumented:", len(new_src), "bytes")


if __name__ == "__main__":
    process_index_html()
    process_pages_content()
    manifest_path = os.path.join(ROOT, "_build", "i18n_strings.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(STRINGS, f, ensure_ascii=False, indent=1)
    print("unique translatable strings:", len(STRINGS))
    print("manifest written to", manifest_path)
