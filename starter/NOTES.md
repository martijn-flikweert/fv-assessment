# Notes (template)

## Keuzes
### Opdracht 1:
- Ik heb gekozen voor 3 methodes `save_state()`, `get_state()` en `remove_state()`. Dit zijn voor mij de basis functies die nodig zijn voor een functionerende state store. Als de applicatie groter wordt, kunnen eventueel extra methodes worden toegevoegd (bijv. `get_all()`, `update_state()`, etc.), maar voor dit project is dit voldoende.
- Ik heb de state store thread safe geïmplementeerd gebruikmakend van RLock. Dit is waarschijnlijk overbodig voor dit project (geen multi-threading), maar het is een simpele toevoeging wat ook weinig tijd kost. 

### Opdracht 2:
- Ik heb de hardcoded klantfilters verwijderd, dit stuk code:
```python
# Legacy customer hardcode (bad)
if state_store.get_state(key = "customer") == "meijer":
    return ["potato"]
```
- Ook heb ik de filters uit de `config.json` verwijderd, deze wordt niet gebruikt en kan voor verwarring zorgen.
- Alle beschikbare crops worden opgehaald uit de config door dit stuk code:
```python
crops = config.get("crops", [])
```
- Alle crops worden al getoond doordat de `get_available_crops` methode crops returned.

### Opdracht 3:
- Ik heb `onionw` toegevoegd aan de config file en daarna de pagina vernieuwd, `onionw` werd juist getoond.

### Opdracht 4:
- Ik heb de hardcoded values verwijderd en hier voor in de plaats halen we nu de data uit de `defects.json`. 
- Ik laat alle visibilities zien behalve als de status `hidden` is en ignore heeft een gele kleur in de UI, echter zat al in de code.
- Ik heb er voor gekozen om voor de crops die geen waarde hebben in het visibility lijstje de default waarde te laten zien.
- Ik heb er voor gekozen om de `defects.json` op te halen in de web_app zodat de `render_defect_sliders` method "clean"
blijft. Ook heb ik onderstaand stuk code toegevoegd aan de HTML script zodat er live updates zijn op het selecteren van een crop:
```javascript
// Reload defects after crop selection
const defects = await getJson("/api/defects");
renderDefects(defects);
```

### Opdracht 5:
- Ik heb de ipc vervangen door de PanelPCClient, waarbij ik er vanuit ga dat dit de communicatie is naar de PC toe. Aangezien er geen PC is om mee te praten geen implementatie kunnen maken van de communicatie hiermee.

### Opdracht 6:
- Ik heb de tests opgedeeld in classes per onderdeel, zodat er duidelijk onderscheid zitten tussen de tests. 
- Ik heb de bestaande tests geupdate met error messages.
- Ik heb tests toegevoegd om de state store implementatie te testen.

### Overige:
- Ik heb de aanname gedaan dat een config file verschilt per klant, waarmee de "customer" dus niet opgeslagen hoeft te worden in de state store, maar direct uit de config gehaald kan worden. De state store is alleen bedoeld voor dynamische waarden die kunnen veranderen (bijv. `selected_crop`).
- .gitignore toegevoegd zodat de `__pycache__` files niet mee gecommit worden.

## Wat zou je doen met meer tijd?
- Extra unit tests toevoegen.
- Een emulator maken van de PC zodat de communicatie hiermee getest kan worden doormiddel van integratietesten.
- De code verder opschonen en meer commments zetten waar nodig.
- De UI mooier maken. 
- De defects file uitbreiden met visibilities voor alle crops.
- Methods toevoegen aan de unit tests, zodat de tests compacter worden.
- Fout situaties testen door het inladen van een (voor die test) verkeerde config of defects json.
- Verder onderzoek gedaan naar Python en de best practices.

## Open vragen
- Ik heb het gevoel dat bij sommige vragen een deel van de implementatie al gedaan was, bijvoorbeeld de aparte status voor "ignore" in the UI. Klopt dit, of mis ik hier de eigenlijke kern van de opdracht?