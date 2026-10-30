#!/usr/bin/env python3
"""Check citations against bib/references.bib and build LaTeX/PDF for all papers.

Usage:
    python3 tools/build_papers.py check          # citation check only
    python3 tools/build_papers.py build [--pdf]  # check, then write .tex (and PDF)

The Markdown sources stay the authoritative, readable versions. The build
links them to the bibliography without changing their prose:

* Author-year citations in the text ("Mayer et al. (1995)", "(Jøsang 2016)")
  are matched to BibTeX keys through the `intextform` field of each entry.
* The hand-written reference list of a paper is matched entry by entry to
  BibTeX keys and must agree with the citations found in the text.
* For LaTeX, the hand-written list is replaced by a bibliography that biblatex
  generates from references.bib (\\nocite of exactly the matched keys); the
  `verification` field is printed after each entry, so status markers such as
  "to be checked" stay visible in the PDF.

Errors (the check fails): a reference-list entry that matches no BibTeX entry
or more than one; a citation in the text whose work is missing from the
paper's reference list. Warnings: listed but never cited; text that looks like
an author-year citation but matches no entry.

Only the Python standard library is used. PDF output needs pandoc, lualatex,
latexmk and biber.
"""

import os
import re
import shutil
import subprocess
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIB = os.path.join(ROOT, "bib", "references.bib")
REPO_URL = "https://github.com/JoeRu/trust-is-engineered/blob/main/"
OUT = os.path.join(ROOT, "build")

# Documents with a reference list: (source, output name, build PDF?)
DOCUMENTS = [
    ("papers/01-evidence-model/paper.md", "paper-1-evidence-model", True),
    ("papers/02-verification-in-organizations/paper.md", "paper-2-verification-in-organizations", True),
    ("papers/03-human-agent-trust/paper.md", "paper-3-human-agent-trust", True),
    ("docs/trust-is-engineered.md", "trust-is-engineered-long-version", True),
    ("docs/case-study-01-populist-techniques.md", "case-study-01-populist-techniques", True),
    ("papers/01-evidence-model/related-work.md", "related-work-1", False),
    ("papers/02-verification-in-organizations/related-work.md", "related-work-2", False),
    ("papers/03-human-agent-trust/related-work.md", "related-work-3", False),
    ("papers/01-evidence-model/whats-new.md", "whats-new-1", False),
    ("papers/02-verification-in-organizations/whats-new.md", "whats-new-2", False),
    ("papers/03-human-agent-trust/whats-new.md", "whats-new-3", False),
]

REF_HEADING = re.compile(r"^(#{2,3}) (?:\d+\. )?References\s*$", re.M)
MATH_FENCE = re.compile(r"^```math\n(.*?)\n```", re.M | re.S)
YEAR = r"(?:19|20)\d\d"


# ---------------------------------------------------------------- bibliography

LATEX_ACCENTS = [("{\\o}", "ø"), ("{\\O}", "Ø"), ("\\o ", "ø"), ("{\\ss}", "ß"), ("{\\aa}", "å"),
                 ("{\\ae}", "æ"), ("{\\AE}", "Æ"), ("\\&", "&"), ("--", "–")]
ACCENT_CMD = {'"': "\u0308", "'": "\u0301", "`": "\u0300", "^": "\u0302", "~": "\u0303", "c": "\u0327", "v": "\u030c"}


def latex_to_unicode(text):
    for a, b in LATEX_ACCENTS:
        text = text.replace(a, b)
    text = re.sub(r"\{?\\([\"'`^~cv])\s?\{?([A-Za-z])\}?\}?",
                  lambda m: unicodedata.normalize("NFC", m.group(2) + ACCENT_CMD[m.group(1)]), text)
    return text.replace("{", "").replace("}", "")


def norm(text):
    """Lowercase ASCII form for matching names."""
    text = latex_to_unicode(text)
    text = text.replace("ø", "o").replace("Ø", "O").replace("æ", "ae").replace("ß", "ss")
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"\\[a-zA-Z]+\s*|[{}\\]", "", text)  # drop LaTeX commands and braces
    return re.sub(r"[^a-z0-9]", "", text.lower())


def load_bib(path):
    """Return {key: {type, fields}} from the one-field-per-line file."""
    entries = {}
    text = open(path, encoding="utf-8").read()
    text = "\n".join(l for l in text.splitlines() if not l.lstrip().startswith("%"))
    for block in re.split(r"\n(?=@)", text):
        m = re.match(r"@(\w+)\{([^,\s]+),\n(.*)\}\s*$", block.strip(), re.S)
        if not m:
            continue
        etype, key, body = m.groups()
        fields = {}
        for fm in re.finditer(r"^\s+(\w+)\s*=\s*(.*?),?\s*$", body, re.M):
            name, value = fm.group(1).lower(), fm.group(2).strip()
            if value.startswith("{") and value.endswith("}"):
                value = value[1:-1]
            fields[name] = value
        entries[key] = {"type": etype.lower(), "fields": fields}
    return entries


def first_author(fields):
    raw = fields.get("author") or fields.get("editor") or ""
    first = re.split(r"\s+and\s+", raw)[0]
    if first.startswith("{"):           # organization in double braces
        return first.strip("{}")
    return first.split(",")[0]


def year_of(fields):
    m = re.search(YEAR, fields.get("year", ""))
    return m.group(0) if m else ""


def citation_patterns(bib):
    """[(regex, key)] built from every intextform of every entry."""
    explicit, generic = [], []
    for key, e in bib.items():
        forms = e["fields"].get("intextform", "")
        if not forms or forms == "not cited in text":
            continue
        for form in forms.split(" | "):
            form = form.strip()
            # "02-verification:Rumpf 2026c" applies only to documents whose path
            # contains "02-verification" (year suffixes differ per document when
            # one author has several works of one year)
            scope = None
            sm = re.match(r"^([\w./-]+):(.+)$", form)
            if sm and not sm.group(1).isdigit():
                scope, form = sm.group(1), sm.group(2).strip()
            m = re.match(r"^(.*?),?(?:\s+\(?|\s*\()(" + YEAR + r")([a-z]?)\)?$", form)
            if m:
                authors, year, suffix = m.group(1).strip(), m.group(2), m.group(3)
                # "&" and "and" are interchangeable; optional comma before the year;
                # year may be in parentheses (narrative citation). A year suffix
                # ("Rumpf 2026b") distinguishes works of one author and year, so a
                # form with a suffix matches only that suffix and a form without
                # one matches only the bare year.
                a = re.escape(authors).replace(r"\&", r"(?:&|and)")
                rx = a + r",?\s+\(?" + year + (suffix if suffix else r"(?![a-z])") + r"\)?"
            else:  # forms without a year, e.g. "NIST SP 800-207", "OWASP 2025 LLM09"
                rx = re.escape(form)
            explicit.append((re.compile(r"(?<![\w-])" + rx + r"(?![\w-])"), key, scope))
    # generic forms from the author field: "A YEAR", "A & B YEAR", "A et al. YEAR",
    # "A, B & C YEAR"; skipped when first author and year are not unique
    seen = {}
    for key, e in bib.items():
        f = e["fields"]
        raw = f.get("author", "")
        if not raw or raw.startswith("{"):
            continue
        sur = latex_to_unicode(first_author(f)).strip()
        y = year_of(f)
        if sur and y:
            seen.setdefault((sur, y), []).append(key)
    for (sur, y), keys in seen.items():
        if len(keys) != 1:
            continue
        name = r"[A-ZÄÖÜÅØ][\w'’\-]+(?: [A-Z][\w'’\-]+)?"
        rx = (re.escape(sur) + r"(?: et al\.|(?:,? (?:&|and) " + name + r")|(?:, " + name + r")+,? (?:&|and) " + name
              + r")?,?\s+\(?" + y + r"[a-z]?\)?")
        generic.append((re.compile(r"(?<![\w-])" + rx + r"(?![\w-])"), keys[0], None))
    # longer patterns first so "Lewicki, McAllister & Bies 1998" wins over "Lewicki 1998"
    # explicit intextform forms win over generic ones ("S. Kim et al. 2024" before
    # "Kim et al. 2024"); within each group longer patterns first
    explicit.sort(key=lambda p: -len(p[0].pattern))
    generic.sort(key=lambda p: -len(p[0].pattern))
    pats = explicit + generic
    return pats


# ---------------------------------------------------------------- documents

def split_references(md):
    """Return (body, reference_section_text or None)."""
    m = REF_HEADING.search(md)
    if not m:
        return md, None
    level = len(m.group(1))
    rest = md[m.end():]
    # the reference section ends at the next heading of the same or higher level
    nxt = re.search(r"^#{1,%d} " % level, rest, re.M)
    end = m.end() + (nxt.start() if nxt else len(rest))
    return md[:m.start()] + md[end:], md[m.start():end]


def reference_lines(section):
    return [l[2:].strip() for l in section.splitlines() if l.startswith("- ")]


def initials(name):
    """'National Institute of Standards and Technology' -> 'nist'."""
    return "".join(w[0] for w in re.findall(r"[A-Z][A-Za-z]*", latex_to_unicode(name))).lower()


def entry_aliases(f):
    aliases = {norm(first_author(f)), norm(f.get("title", ""))[:40]}
    raw = f.get("author", "")
    if raw.startswith("{"):
        aliases.add(initials(raw))
    for form in f.get("intextform", "").split(" | "):
        form = re.sub(r"^[\w./-]+:", "", form.strip())
        aliases.add(norm(re.split(r",?\s*\(?" + YEAR, form)[0]))
    aliases.discard("")
    return aliases


def match_reference_line(line, bib):
    """BibTeX keys whose first author (or alias) and year match a reference-list line."""
    m = re.search(r"\((" + YEAR + r")[a-z]?(?:[,)]|\s)", line) or re.search(r"\b(" + YEAR + r")\b", line)
    year = m.group(1) if m else None
    lead = norm(line.split("(")[0].split(",")[0])
    token = re.split(r"[\s,(]", line.strip())[0]
    acronym = norm(token) if token.isupper() and len(token) >= 2 else None
    if len(lead) < 2:
        return []
    hits = []
    for key, e in bib.items():
        f = e["fields"]
        if year is not None and year_of(f) and year_of(f) != year:
            continue
        if year is None and year_of(f):
            continue
        aliases = entry_aliases(f)
        ok = any(len(al) >= 2 and (lead.startswith(al) or al.startswith(lead)) for al in aliases)
        if not ok and acronym:
            ok = any(al.startswith(acronym) for al in aliases)
        if ok:
            hits.append(key)
    if len(hits) > 1:  # several works of one author and year: the line that
        # contains one entry's full title (longest wins) decides; otherwise
        # compare title words
        nline = norm_words(line)
        full = [k for k in hits if norm_words(bib[k]["fields"].get("title", "")) in nline]
        if full:
            full.sort(key=lambda k: -len(bib[k]["fields"].get("title", "")))
            if len(full) == 1 or len(bib[full[0]]["fields"]["title"]) > len(bib[full[1]]["fields"]["title"]):
                return [full[0]]
        words = [w for w in re.findall(r"[a-z]{5,}", nline)]
        scored = []
        for k in hits:
            t = norm_words(bib[k]["fields"].get("title", ""))
            scored.append((sum(w in t for w in words), k))
        scored.sort(reverse=True)
        if scored[0][0] > 0 and (len(scored) == 1 or scored[0][0] > scored[1][0]):
            hits = [scored[0][1]]
    return hits


def norm_words(text):
    text = unicodedata.normalize("NFKD", text)
    return "".join(c for c in text if not unicodedata.combining(c)).lower()


SUSPECT = re.compile(
    r"(?<![\w-])[A-ZÄÖÜ][A-Za-zÀ-ÿ'’\-]+(?: et al\.)?(?:,? (?:& |and )?[A-ZÄÖÜ][A-Za-zÀ-ÿ'’\-]+)*,? \(?"
    + YEAR + r"[a-z]?\)?")
NOT_CITATIONS = re.compile(
    r"^(?:Since|In|Version|Edition|October|January|February|March|April|May|June|July|"
    r"August|September|November|December|As|From|Stand|Draft|Act|Art|Regulation|ISO|IEC|"
    r"Phase|Section|Table|Figure|By|Before|After|Until|Top|The|Year|Studies|Report)\b")


EXTRA_YEARS = re.compile(r"(?:,\s*(?:19|20)\d\d[a-z]?)+")


def match_one(text, pats):
    """Key of the citation pattern that matches the whole text, or None."""
    for rx, key in pats:
        m = rx.search(text)
        if m and m.start() == 0 and m.end() == len(text):
            return key
    return None


def find_citations(text, pats):
    """Return (found {key: form}, unresolved suspects, unmatched grouped years).

    Grouped citations such as "Debenedetti et al. (2024, 2025)" or
    "Debenedetti et al. 2024, 2025" are expanded: every further year is
    checked with the same authors and must match an entry of its own.
    """
    found, spans, unmatched = {}, [], []
    for rx, key in pats:
        for m in rx.finditer(text):
            if any(s <= m.start() < e for s, e in spans):
                continue
            end = m.end()
            found.setdefault(key, m.group(0))
            extra = EXTRA_YEARS.match(text, m.end())
            if extra:
                head = re.sub(r"[\s(]*(?:19|20)\d\d[a-z]?\)?$", "", m.group(0))
                for y in re.findall(r"(?:19|20)\d\d[a-z]?", extra.group(0)):
                    form = head + " " + y
                    k = match_one(form, pats)
                    if k:
                        found.setdefault(k, form)
                    else:
                        unmatched.append(form)
                end = extra.end()
            spans.append((m.start(), end))
    unresolved = []
    for m in SUSPECT.finditer(text):
        if any(s <= m.start() < e or s < m.end() <= e for s, e in spans):
            continue
        if NOT_CITATIONS.match(m.group(0)):
            continue
        unresolved.append(m.group(0))
    return found, sorted(set(unresolved)), sorted(set(unmatched))


def check_document(path, bib, pats):
    md = open(os.path.join(ROOT, path), encoding="utf-8").read()
    pats = [(rx, key) for rx, key, scope in pats if scope is None or scope in path]
    body, refs = split_references(md)
    errors, warnings = [], []
    listed = {}
    if refs is None:
        errors.append("no reference section found")
    else:
        for line in reference_lines(refs):
            hits = match_reference_line(line, bib)
            if len(hits) == 1:
                listed[hits[0]] = line
            elif not hits:
                errors.append("reference not in bib: " + line[:90])
            else:
                errors.append("reference ambiguous (%s): %s" % (", ".join(hits), line[:70]))
        prose = "\n".join(l for l in refs.splitlines() if not l.startswith("- ") and not l.startswith("#"))
        for key in find_citations(prose, pats)[0]:
            listed.setdefault(key, "(adopted)")
    cited, unresolved, unmatched = find_citations(body, pats)
    for u in unmatched:
        errors.append("grouped citation year without bib match: " + u)
    for key, form in sorted(cited.items()):
        if refs is not None and key not in listed:
            errors.append("cited but not in reference list: %s (%s)" % (form, key))
    for key in sorted(set(listed) - set(cited)):
        warnings.append("listed but not found in text: " + key)
    for u in unresolved:
        warnings.append("possible citation without bib match: " + u)
    keys = sorted(set(listed) | set(cited))
    return md, keys, errors, warnings


# ---------------------------------------------------------------- LaTeX build

def reference_prose(md):
    """Explanatory prose of the reference section (legend, notes), without the list."""
    _, refs = split_references(md)
    if not refs:
        return ""
    lines = refs.splitlines()[1:]  # drop the heading
    keep = [l for l in lines if not l.startswith("- ") and not l.startswith("#")]
    return "\n".join(keep).strip()


def to_pandoc_markdown(md, src_path, keys, outdir, name):
    body, _ = split_references(md)
    # GitHub ```math blocks -> display math
    body = MATH_FENCE.sub(lambda m: "$$\n" + m.group(1).strip() + "\n$$", body)
    # title from the first H1, otherwise the first H2 (Case Study 1)
    m = re.search(r"^# (.+)$", body, re.M) or re.search(r"^## (.+)$", body, re.M)
    title = m.group(1).strip() if m else os.path.basename(src_path)
    if m:
        body = body[:m.start()] + body[m.end():]
    src_dir = os.path.dirname(src_path)
    os.makedirs(os.path.join(outdir, "figures"), exist_ok=True)

    def relink(match):
        text, target = match.group(1), match.group(2)
        if re.match(r"^[a-z]+:", target) or target.startswith("#"):
            return match.group(0)
        path, _, anchor = target.partition("#")
        full = os.path.normpath(os.path.join(ROOT, src_dir, path))
        rel = os.path.relpath(full, ROOT).replace(os.sep, "/")
        if path.lower().endswith((".png", ".jpg", ".jpeg", ".pdf")):
            shutil.copy(full, os.path.join(outdir, "figures", os.path.basename(full)))
            return "%s(figures/%s)" % (text, os.path.basename(full))
        return "%s(%s%s)" % (text, REPO_URL, rel + ("#" + anchor if anchor else ""))

    body = re.sub(r"(!?\[[^\]]*\])\(([^)\s]+)\)", relink, body)
    body = body.rstrip() + "\n"

    # the preamble and, if present, the legend of the reference list travel with the .tex
    shutil.copy(os.path.join(ROOT, "tools", "latex", "preamble.tex"), os.path.join(outdir, "preamble.tex"))
    includes = [r"\input{preamble.tex}"]
    prose = reference_prose(md)
    if prose:
        legend = subprocess.run(["pandoc", "--from", "markdown", "--to", "latex"], input=prose,
                                capture_output=True, text=True, check=True).stdout.strip()
        open(os.path.join(outdir, "bibnote.tex"), "w", encoding="utf-8").write(
            "\\AddToHook{package/biblatex/after}{%\n  \\defbibnote{legend}{" + legend
            + "}%\n  \\DeclarePrintbibliographyDefaults{prenote=legend}%\n}\n")
        includes.append(r"\input{bibnote.tex}")
    meta = [
        "---",
        "title: " + yaml_str(title),
        "lang: en-US",
        "documentclass: article",
        "classoption: [11pt, a4paper]",
        "geometry: margin=2.5cm",
        "mainfont: DejaVu Serif",
        "sansfont: DejaVu Sans",
        "monofont: DejaVu Sans Mono",
        "mainfontoptions: [Scale=0.92]",
        "colorlinks: true",
        "biblio-title: References",
        "biblatexoptions: [style=authoryear, maxbibnames=99, maxcitenames=2, uniquename=false, uniquelist=false, backend=biber]",
        "bibliography: " + yaml_str(name + ".bib"),
        "nocite: |",
        "  " + ", ".join("@" + k for k in keys),
        "header-includes:",
    ] + ["  - " + yaml_str(i) for i in includes] + ["---", ""]
    return "\n".join(meta) + body


def yaml_str(s):
    return "'" + s.replace("'", "''") + "'"


def build(doc, name, keys, pdf):
    """Write a self-contained folder build/<name>/: .md, .tex, subset .bib,
    preamble, legend and figures; compiles anywhere with LuaLaTeX and biber."""
    outdir = os.path.join(OUT, name)
    os.makedirs(outdir, exist_ok=True)
    md = open(os.path.join(ROOT, doc), encoding="utf-8").read()
    write_subset_bib(keys, os.path.join(outdir, name + ".bib"))
    pmd = os.path.join(outdir, name + ".md")
    open(pmd, "w", encoding="utf-8").write(to_pandoc_markdown(md, doc, keys, outdir, name))
    subprocess.run(["pandoc", name + ".md", "--from", "markdown+tex_math_dollars-implicit_figures",
                    "--standalone", "--biblatex", "--pdf-engine=lualatex", "-o", name + ".tex"],
                   cwd=outdir, check=True)
    if pdf:
        subprocess.run(["latexmk", "-lualatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-file-line-error", name + ".tex"], cwd=outdir, check=True)
        os.makedirs(os.path.join(OUT, "pdf"), exist_ok=True)
        shutil.copy(os.path.join(outdir, name + ".pdf"), os.path.join(OUT, "pdf", name + ".pdf"))


def write_subset_bib(keys, path):
    """Per-document .bib with exactly the cited entries (for submissions)."""
    text = open(BIB, encoding="utf-8").read()
    blocks = {}
    for block in re.split(r"\n(?=@)", text):
        m = re.match(r"@\w+\{([^,\s]+),", block.strip())
        if m:
            blocks[m.group(1)] = block.strip().split("\n\n%")[0].strip()
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("% Subset of bib/references.bib for this document (generated).\n\n")
        for k in keys:
            fh.write(blocks[k] + "\n\n")


# ---------------------------------------------------------------- main

def main(argv):
    mode = argv[1] if len(argv) > 1 else "check"
    pdf = "--pdf" in argv
    bib = load_bib(BIB)
    pats = citation_patterns(bib)
    failed = False
    results = []
    for doc, name, makes_pdf in DOCUMENTS:
        if not os.path.exists(os.path.join(ROOT, doc)):
            print("\n== %s\n  ERROR   configured document is missing" % doc)
            failed = True
            continue
        md, keys, errors, warnings = check_document(doc, bib, pats)
        print("\n== %s: %d references matched, %d errors, %d warnings"
              % (doc, len(keys), len(errors), len(warnings)))
        for e in errors:
            print("  ERROR   " + e)
        for w in warnings:
            print("  warning " + w)
        failed = failed or bool(errors)
        results.append((doc, name, keys, makes_pdf))
    if failed:
        print("\nCitation check failed.")
        return 1
    print("\nCitation check passed.")
    if mode == "build":
        for doc, name, keys, makes_pdf in results:
            if makes_pdf:
                build(doc, name, keys, pdf)
                print("built " + name + (" (pdf)" if pdf else " (tex)"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
