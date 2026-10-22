# Bibliography check report

18 October 2026. Result of converting Chapter 16 of the long version into `references.bib` and of the related-work search for Papers 1–3. Nothing in the long version or the papers was changed on the basis of this report; each point needs a decision by the author.

## 1. Entries of Chapter 16 that contradict an authoritative source

Real conflicts, to be corrected in Chapter 16, in the papers and in `references.bib` together:

| Key | Paper says | Source says |
| --- | --- | --- |
| `haselhuhn2010` | Psychological Science 21(2), 181–183 | Crossref: 21(5), 645–648; issue 21(2) has no article by these authors at 181–183 |
| `clifton2019` | pages 82–101 | Crossref: 82–99 |
| `mattavelli2025` | 2025 | online first 26 June 2025; print issue 52(9) dated September 2026 — decide which year to cite |
| `fbi2024` | "Internet Crime Report 2024" | the PDF is titled "2024 IC3 Annual Report", released April 2025 |
| `uslaner2002` | 2002 | publisher 2002 (print); Crossref lists 2001 — 2002 is fine |

Title given in short form only (not an error, but a full title is better for the printed reference list): `bond1996`, `cialdini1990`, `marques1988`, `coppock2022`, `fetchenhauer2010`, `wood2019`, `yousif2019`, `chesney2019`, `schiff2025`, `bsi2017`.

## 2. Fields that could not be confirmed

| Key | Missing |
| --- | --- |
| `josang2002` | pages, DOI (conference paper) |
| `asch1951` | pages |
| `chesney2019` | issue number |
| `hogarth2001` | ISBN of the 2001 edition |

## 3. Chapter 16 entries not cited in the running text

`castelfranchi2010`, `marsh1994`, `fazio2015`, `bsi2017`. Castelfranchi & Falcone and Marsh are now used in the related-work document of Paper 1.

## 4. New references from the related-work documents

77 new entries (Part 2 of `references.bib`). 73 are marked `secondary citation` (abstract or publisher page read), 4 `to be checked` (existence and metadata confirmed only): `devisser2020`, `kish1965`, `clark1987`, `hoffman2006`. Five are preprints without a confirmed peer-reviewed venue: `debenedetti2025`, `ehtesham2025`, `huang2025`, `south2025`, `wallace2024`. Small metadata conflicts: `unkelbach2017` (last page), `clark1987` (page range), `cherdantseva2016` (author order).

## 5. Findings that concern the content of the long version

The related-work search found prior work that bears on statements in the long version. These are not bibliographic errors; they are candidates for the next content revision (branch `v0.7-…`):

- **Section 4.3, evidence model.** The Beta Reputation System (Jøsang & Ismail 2002) already contains a forgetting factor and the discounting of ratings by the rater's reputation. The text should credit this explicitly instead of reading as if temporal decay were added by the model (related-work-1, line of work "computational trust").
- **Section 4.7, n_eff.** The formula has the form of Kish's design effect (Kish 1965, to be checked); attribution is missing.
- **H16 evidence status ("no measurement of τ_I in security contexts known").** Zhang, Reithel & Li (2009) report that perceived technical protection lowers the intention to comply with security policy and recommend stressing the limits of technical protection (close to S22). The status row should be revised (related-work-2).
- **H17 / Section 7.10, former 7.9 ("hardly measured in security contexts"; narrowed in v0.7).** Brink, Eller & Gan (2015) and Paravastu et al. (2018) measured diffusion of responsibility in fraud and security reporting. H17 should be narrowed to verification coverage per action class (related-work-2).
- **H18.** Herath & Rao (2009) and Das et al. (2014) show peer influence and social proof in security behavior; the status row understates this (related-work-2).
- **Section 10.7 / H14, independent verifiers.** Kim et al. (2025, `kim2025a`) report that errors of capable language models remain correlated across providers; "different model, different provider" as the remedy should be weakened (related-work-3).

All new sources above are `secondary citation`: their statements rest on abstracts and must be checked against the full text before the long version relies on them.
