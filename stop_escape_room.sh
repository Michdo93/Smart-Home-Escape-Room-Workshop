#!/bin/bash

NODE_RED_PROCESS="/home/$USER/.nvm/versions/node/v16.13.2/bin/node-red"
PYTHON_SCRIPT="/home/$USER/Smart-Home-Escape-Room-Workshop/Python/Laptop/stop_escape_room.py"
SELENIUM_PROCESS="selenium-server"

# Prüfen, ob Node-RED lokal läuft
function is_node_red_running() {
    pgrep -f "$NODE_RED_PROCESS" > /dev/null 2>&1
    return $?
}

# Prüfen, ob Selenium lokal läuft
function is_selenium_running() {
    pgrep -f "$SELENIUM_PROCESS" > /dev/null 2>&1
    return $?
}

# Python-Skript ausführen
echo "Stoppe Escape Room..."
python3 "$PYTHON_SCRIPT"

# Selenium-Server beenden, wenn er läuft
if is_selenium_running; then
    echo "Beende Selenium-Server..."
    pkill -f "$SELENIUM_PROCESS"
    if [ $? -eq 0 ]; then
        echo "Selenium-Server wurde erfolgreich beendet."
    else
        echo "Fehler: Selenium-Server konnte nicht beendet werden."
    fi
else
    echo "Selenium-Server läuft nicht. Nichts zu beenden."
fi

# Node-RED beenden, wenn es läuft
if is_node_red_running; then
    echo "Beende Node-RED..."
    pkill -f "$NODE_RED_PROCESS"
    if [ $? -eq 0 ]; then
        echo "Node-RED wurde erfolgreich beendet."
    else
        echo "Fehler: Node-RED konnte nicht beendet werden."
    fi
else
    echo "Node-RED läuft nicht. Nichts zu beenden."
fi
