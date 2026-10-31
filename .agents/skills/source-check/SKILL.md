---
name: source-check
description: Prüft Literaturangaben und zitierte Aussagen im öffentlichen Forschungsrepo Trust Is Engineered gegen Originalquellen und pflegt ihren Verifikationsstatus.
---

# Quellen im Paper prüfen

Lies `AGENTS.md` im gemeinsamen Hauptordner, `CLAUDE.md` dieses Repos und `bib/README.md`. Maßgeblich sind die englische Langfassung `docs/trust-is-engineered.md` und `bib/references.bib`; die deutsche Archivfassung nicht ändern.

- Suche den Eintrag in Kapitel 16, der BibTeX-Datei und allen zitierenden Stellen der Langfassung, der drei Paper und der Fallstudie. `bib/check-report.md` enthält bekannte Abweichungen.
- Prüfe bibliografische Daten anhand von DOI, Verlag oder Original. Prüfe die *zitierte Aussage* am tatsächlich gelesenen Originaltext. Abstract, Suchauszug und Sekundärzitat reichen nicht für „verified“.
- Halte fest, was gelesen wurde, welche Stellen es stützt oder nicht stützt, und welche Daten korrigiert wurden. Bei fehlendem Volltext den schwächeren Status beibehalten.
- Ändere Verifikationsvermerke in Langfassung und `bib/references.bib` gemeinsam; gleiche betroffene Paper ab. Entferne keinen Statusvermerk ohne begründeten Ersatz.
- Führe bei Änderungen an Zitaten oder Literatur `python tools/build_papers.py check` aus. Berichte verbleibende Unsicherheit ausdrücklich.

Neue inhaltliche Behauptungen oder eine neue Version fallen zusätzlich unter `.agents/skills/paper-cascade/SKILL.md` im gemeinsamen Hauptordner.
