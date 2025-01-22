from openhab_test_suite import OpenHABConnector, ItemTester

# Establishing connection to the OpenHAB API
connector = OpenHABConnector("http://<your_ip>:8080", "<username>", "<password>")

# Instantiating the ItemTester
tester = ItemTester(connector)

# List of items
itemsToCheck = [
    ("iMultimedia_Homematic_Schaltglas1_Schalten", "Switch", "ON", "ON"),
    ("iMultimedia_Homematic_Schaltglas2_Schalten", "Switch", "ON", "ON"),
    ("iMultimedia_Homematic_Fenster1_Position", "String", None, ["OPEN", "CLOSED", "TILTED"]),
    ("iMultimedia_Homematic_Fenster2_Position", "String", None, ["OPEN", "CLOSED", "TILTED"]),
    ("iMultimedia_Homematic_Fenster3_Position", "String", None, ["OPEN", "CLOSED", "TILTED"]),
    ("iMultimedia_Hue_Lampe1_Schalter", "Switch", "ON", "ON"),
    ("iMultimedia_Hue_Lampe1_Farbe", "Color", "255,0,0", "255,0,0"),
    ("iMultimedia_Hue_Lampe2_Schalter", "Switch", "ON", "ON"),
    ("iMultimedia_Hue_Lampe2_Farbe", "Color", "255,0,0", "255,0,0"),
    ("iMultimedia_Hue_Lampe3_Schalter", "Switch", "ON", "ON"),
    ("iMultimedia_Hue_Lampe3_Farbe", "Color", "255,0,0", "255,0,0"),
    ("iMultimedia_Hue_Lampe4_Schalter", "Switch", "ON", "ON"),
    ("iMultimedia_Hue_Lampe4_Farbe", "Color", "255,0,0", "255,0,0"),
    ("iMultimedia_Hue_Lampe5_Schalter", "Switch", "ON", "ON"),
    ("iMultimedia_Hue_Lampe5_Farbe", "Color", "255,0,0", "255,0,0"),
    ("iMultimedia_Hue_Lampe6_Schalter", "Switch", "ON", "ON"),
    ("iMultimedia_Hue_Lampe6_Farbe", "Color", "255,0,0", "255,0,0"),
    ("iMultimedia_Homematic_Drucktaster_Kurz1", "Switch", "ON", "ON"),
    ("iMultimedia_Homematic_Drucktaster_Lang1", "Switch", "ON", "ON"),
    ("iBad_Hue_Lampe1_Schalter", "Switch", "ON", "ON"),
    ("iBad_Hue_Lampe2_Schalter", "Switch", "ON", "ON"),
    ("iBad_Hue_Lampe3_Schalter", "Switch", "ON", "ON"),
    ("iBad_Hue_Lampe4_Schalter", "Switch", "ON", "ON"),
    ("iBad_Hue_Lampe5_Schalter", "Switch", "ON", "ON"),
    ("iBad_Hue_Lampe6_Schalter", "Switch", "ON", "ON"),
    ("iIoT_Hue_Lampe1_Farbe", "Color", "255,0,0", "255,0,0"),
    ("iIoT_Hue_Lampe2_Farbe", "Color", "255,0,0", "255,0,0"),
    ("iIoT_Hue_Lampe3_Farbe", "Color", "255,0,0", "255,0,0"),
    ("iIoT_Hue_Lampe4_Farbe", "Color", "255,0,0", "255,0,0"),
    ("iIoT_Hue_Lampe5_Farbe", "Color", "255,0,0", "255,0,0"),
    ("iIoT_Hue_Lampe6_Farbe", "Color", "255,0,0", "255,0,0"),
    ("iIoT_Hue_Lampen_Schalter", "Switch", "ON", "ON"),
]

# Check item states
for itemName, itemType, command, expectedState in itemsToCheck:
    if itemType == "Color":
        print(f"{itemName}: ", tester.testColor(itemName=itemName, command=command, expectedState=expectedState))
    elif itemType == "Contact":
        print(f"{itemName}: ", tester.testContact(itemName=itemName, update=command, expectedState=expectedState))
    elif itemType == "DateTime":
        print(f"{itemName}: ", tester.testDateTime(itemName=itemName, command=command, expectedState=expectedState))
    elif itemType == "Dimmer":
        print(f"{itemName}: ", tester.testDimmer(itemName=itemName, command=command, expectedState=expectedState))
    elif itemType == "Location":
        print(f"{itemName}: ", tester.testLocation(itemName=itemName, update=command, expectedState=expectedState))
    elif itemType == "Number":
        print(f"{itemName}: ", tester.testNumber(itemName=itemName, command=command, expectedState=expectedState))
    elif itemType == "Player":
        print(f"{itemName}: ", tester.testPlayer(itemName=itemName, command=command, expectedState=expectedState))
    elif itemType == "Rollershutter":
        print(f"{itemName}: ", tester.testRollershutter(itemName=itemName, command=command, expectedState=expectedState))
    elif itemType == "String":
        print(f"{itemName}: ", tester.testString(itemName=itemName, command=command, expectedState=expectedState))
    elif itemType == "Switch":
        print(f"{itemName}: ", tester.testSwitch(itemName=itemName, command=command, expectedState=expectedState))
