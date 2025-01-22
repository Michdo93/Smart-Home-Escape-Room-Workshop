from openhab import CRUD

# Verbindung zu openHAB herstellen
crud = CRUD("", "", "")  # Zugangsdaten anpassen

# Liste der Items
items_to_check = [
    "iMultimedia_Homematic_Schaltglas1_Schalten",
    "iMultimedia_Homematic_Schaltglas2_Schalten",
    "iMultimedia_Homematic_Fenster1_Position",
    "iMultimedia_Homematic_Fenster2_Position",
    "iMultimedia_Homematic_Fenster3_Position",
    "iMultimedia_Hue_Lampe1_Schalter",
    "iMultimedia_Hue_Lampe1_Farbe",
    "iMultimedia_Hue_Lampe2_Schalter",
    "iMultimedia_Hue_Lampe2_Farbe",
    "iMultimedia_Hue_Lampe3_Schalter",
    "iMultimedia_Hue_Lampe3_Farbe",
    "iMultimedia_Hue_Lampe4_Schalter",
    "iMultimedia_Hue_Lampe4_Farbe",
    "iMultimedia_Hue_Lampe5_Schalter",
    "iMultimedia_Hue_Lampe5_Farbe",
    "iMultimedia_Hue_Lampe6_Schalter",
    "iMultimedia_Hue_Lampe6_Farbe",
    "iMultimedia_Homematic_Drucktaster_Kurz1",
    "iMultimedia_Homematic_Drucktaster_Lang1",
    "iBad_Hue_Lampe1_Schalter",
    "iBad_Hue_Lampe2_Schalter",
    "iBad_Hue_Lampe3_Schalter",
    "iBad_Hue_Lampe4_Schalter",
    "iBad_Hue_Lampe5_Schalter",
    "iBad_Hue_Lampe6_Schalter",
    "iIoT_Hue_Lampe1_Farbe",
    "iIoT_Hue_Lampe2_Farbe",
    "iIoT_Hue_Lampe3_Farbe",
    "iIoT_Hue_Lampe4_Farbe",
    "iIoT_Hue_Lampe5_Farbe",
    "iIoT_Hue_Lampe6_Farbe",
    "iIoT_Hue_Lampen_Schalter",
]

# Ergebnisse speichern
states = {}
failed_items = []

# Zustände der Items abrufen
for item in items_to_check:
    try:
        state = crud.getState(item)
        states[item] = state
    except Exception as e:
        print(f"Fehler beim Abrufen des Zustands von {item}: {e}")
        failed_items.append(item)

# Ergebnisse ausgeben
print("Zustände der Items:")
for item, state in states.items():
    print(f"{item}: {state}")

if failed_items:
    print("\nFehlgeschlagene Abfragen:")
    for item in failed_items:
        print(item)

# Sitzung schließen
crud.close()
