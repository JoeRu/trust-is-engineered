# Trust Is Engineered — Claude Context

Arbeitspapier *Trust Is Engineered* (`docs/trust-is-engineered.md`) mit
Begleitpapieren (`docs/case-study-*.md`) und Abbildungen (`docs/figures/`).
**Sprache: Englisch.** Ab v0.6 ist die englische Fassung maßgeblich; alle
Paper werden auf Englisch geschrieben. Das deutsche Original der v0.6 liegt
eingefroren unter `docs/de/` und wird nicht mehr geändert.
Das Paper ist als **DRAFT** gekennzeichnet (Hinweis oben in README, Paper und
Fallstudie) — den Hinweis nicht entfernen, solange Johannes keine Fassung freigibt.
Lizenz: CC BY 4.0 (`LICENSE`) für Text und Abbildungen. Code, falls er
hinzukommt, erhält eine eigene Softwarelizenz (vorgesehen: Apache 2.0) in
seinem Ordner, nicht CC BY.
Das Repository ist **öffentlich**: Jeder Commit, jede Commit-Nachricht und
jeder PR-Text ist sofort sichtbar.

## Belegdisziplin

- Jede Aussage behält ihren Status: Grundannahme **G** (core assumption) und
  Hypothese **H** (Kapitel 11), Vorhersage **V** (prediction, Kapitel 12),
  Regel **S** (rule, Kapitel 14), Stand v0.6. Eine Hypothese bleibt eine
  Hypothese. Die Kennungen G, H, V, S bleiben trotz englischer Sprache stabil.
- Nie behaupten oder andeuten, das Modell oder ein Training sei validiert.
- Kein Scoring von Personen für Entscheidungen Dritter.
- Literaturvermerke in Kapitel 16: "(to be checked)" = ungeprüft,
  "(secondary citation)" = nur über Abstracts oder zitierende Arbeiten gesehen,
  "(verified YYYY-MM-DD)" = am Volltext geprüft. Einen Vermerk nie
  einfach löschen; die Legende in Kapitel 16 definiert sie.

## Abbildungen

- Die Abbildungen werden mit `docs/figures/src/make_figures.py` erzeugt
  (nur matplotlib). Änderungen an Abbildungen im Skript vornehmen und das
  Skript neu laufen lassen, nie die PNG-Dateien von Hand bearbeiten.

## Änderungen

- Korrekturen an Literaturangaben direkt auf `main`
  (`docs(paper): reference check <entries>`).
- Inhaltliche Überarbeitungen auf einem Branch `v<next>-<thema>` mit PR;
  Johannes merged. Versionszeile, Kapitel 0 ("Changes in v<next>") und die
  Kapiteltabelle in `README.md` mitziehen, ebenso `version` und
  `date-released` in `CITATION.cff` sowie die Version im Zitiervorschlag
  des README.
- Keine internen Host-, Pfad- oder Personennamen in Dateien, Commits oder PRs.
