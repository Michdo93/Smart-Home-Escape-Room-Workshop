#!/bin/bash

NODE_RED_PROCESS="/home/$USER/.nvm/versions/node/v16.13.2/bin/node-red"
PYTHON_SCRIPT="/home/$USER/Smart-Home-Escape-Room-Workshop/Python/Laptop/stop_escape_room.py"

# Prüfen, ob Node-RED lokal läuft
function is_node_red_running() {
    pgrep -f "$NODE_RED_PROCESS" > /dev/null 2>&1
    return $?
}

# Python-Skript ausführen
echo "Stoppe Escape Room..."
python3 "$PYTHON_SCRIPT"

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
