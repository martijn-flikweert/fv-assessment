# Assessment – Panel PC Refactor (max 4 uur)

Doel: beoordeel hoe je legacy UI/IPC code structureert, testbaar maakt en configuratie‑gedreven maakt.

**Tijdslimiet:** max 4 uur (stop op tijd en noteer wat je zou doen als je meer tijd had).

## Context
In `assesment/starter/` staat een sterk vereenvoudigde Panel PC codebase. Deze bevat:
- hardcoded crop‑filters per klant
- global dict state
- defect‑sliders met index‑based access
- een simpele IPC stub

## Opdracht
1) **Vervang globale state**
   - Maak een `StateStore` interface + concrete implementatie.
   - Verwijder directe `GLOBAL_D` access in de UI.

2) **Crop‑selectie configuratie‑gedreven**
   - Haal beschikbare crops uit `config.json`.
   - Verwijder hardcoded klantfilters (zoals “meijer only potato”).
   - Toon **alle crops** uit config.

3) **Nieuwe crop toevoegen via config**
   - Voeg `onionw` toe **alleen** in `config.json`.
   - Zorg dat de UI dit direct toont zonder code‑wijzigingen.

4) **Defect‑sliders op basis van `defects.json`**
   - Gebruik de defect‑catalogus (keys) i.p.v. vaste indexen.
   - Toon alleen “visible” defecten.
   - “ignore” moet in de UI een aparte status krijgen (bijv. label).

5) **IPC‑laag opschonen**
   - Zorg dat UI via een `PanelPCClient` praat met de backend.
   - Geen directe prints in de UI‑logica.

6) **Tests**
   - Voeg minimaal 1 test toe (config loading of defect‑filtering).

## Beperkingen
- Geen externe dependencies installeren.
- Houd het klein en pragmatisch.
- Gebruik alleen standaard Python 3.

## Deliverables
- Aangepaste code in `assesment/starter/`
- `NOTES.md` met:
  - korte uitleg van je keuzes
  - wat je zou verbeteren met meer tijd

## Hoe runnen
```bash
cd assesment/starter
python app.py
```
Open in browser: http://127.0.0.1:8000

Tests (optioneel):
```bash
python -m unittest
```

## Beoordelingscriteria
- Duidelijke scheiding UI / state / config / IPC
- Config‑gedreven gedrag (nieuwe crop zonder codewijziging)
- Leesbaarheid en pragmatische refactor
- Basale testbaarheid
