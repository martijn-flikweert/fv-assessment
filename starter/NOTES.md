# Notes (template)

## Keuzes
### Opdracht 1:
- Ik heb gekozen voor 3 methodes `save_state()`, `get_state()` en `remove_state()`. Dit zijn voor mij de basis functies die nodig zijn voor een functionerende statestore. Als de applicatie groter wordt, kunnen eventueel extra methodes worden toegevoegd (bijv. `get_all()`, `update_state()`, etc.), maar voor dit project is dit voldoende.
- Ik heb de state store thread safe geïmplementeerd gebruikmakend van RLock. Dit is waarschijnlijk overbodig voor dit project (geen multi-threading), maar het is een simpele toevoeging wat ook weinig tijd kost. 

### Opdracht 2:
- Ik heb de hardcoded klantfilters verwijderd, dit stuk code:
```
# Legacy customer hardcode (bad)
if state_store.get_state(key = "customer") == "meijer":
    return ["potato"]
```
- Ook heb ik de filters uit de `config.json` verwijderd. Dit wordt niet gebruikt en kan voor verwarring zorgen.
- Alle beschikbare crops worden alle opgehaald uit de config door dit stuk code:
```
crops = config.get("crops", [])
```
- Alle crops worden al getoond doordat de `get_available_crops` methode crops returned.

### Overige:
- Ik heb de aanname gedaan dat een config file verscheelt per klant, waarmee de "customer" dus niet opgeslagen hoeft te worden in de state store, maar direct uit de config gehaald kan worden. De state store is alleen bedoeld voor dynamische waarden die kunnen veranderen (bijv. `selected_crop`).
- .gitignore toegevoegd zodat de `__pycache__` files niet mee gecommit worden.

## Wat zou je doen met meer tijd?
- ...

## Open vragen
- ...