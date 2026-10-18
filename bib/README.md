# Bibliography

`references.bib` is the single bibliography for the long version and the three papers. It holds every entry of Chapter 16 of the long version, in the same order and grouped by the same sub-headings, plus the references that the related-work documents add (last section of the file).

## Keys

`<first-author-lastname><year>` in lowercase ASCII (`josang2016`, `vanlange2014`); a, b … for several works of the same first author and year. Organizations and legal sources use an acronym (`nist2020`, `owasp2025`, `euaiact2024`).

## Custom fields

LaTeX tools (biber, citeproc) ignore these fields; they carry the evidence discipline of the paper.

| Field | Meaning |
| --- | --- |
| `verification` | The status marker of the entry, copied from the paper: `to be checked`, `secondary citation`, `checked against full text`, `verified YYYY-MM-DD`, an annotated variant (e.g. `author list to be checked`), or `unmarked` if the paper's entry carries no marker. Entries added by the related-work documents carry `secondary citation` (abstract or publisher page read) or `to be checked`. Looking up bibliographic data never changes this field. |
| `intextform` | How the long version cites the work in running text (several forms separated by ` \| `); `not cited in text` if it appears only in the reference list. |
| `metadatasource` | Where fields missing from the paper's entry were completed from (e.g. Crossref via DOI). |
| `discrepancy` | An authoritative source differs from the paper's entry. The normal fields keep the paper's value; this field describes the conflict. See `check-report.md`. |
| `note = {incomplete: …}` | A field that could not be confirmed and was left out. |

## Rules

- A status changes only after checking the full text: then set `verification = {verified YYYY-MM-DD}` here **and** the marker in Chapter 16 of the long version (and in the papers) in the same commit.
- Resolve a `discrepancy` by correcting the entry in Chapter 16 and here together, then delete the field.
- New references go into the last section of `references.bib` with their status; never cite a work in a paper without an entry here.
