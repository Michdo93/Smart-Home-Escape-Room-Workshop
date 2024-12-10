#!/bin/bash

NODE_RED_PROCESS="/home/$USER/.nvm/versions/node/v16.13.2/bin/node-red"
NODE_RED_SCRIPT="/home/$USER/Smart-Home-Escape-Room-Workshop/start_node_red.sh"
PYTHON_SCRIPT="/home/$USER/Smart-Home-Escape-Room-Workshop/Python/Laptop/start_escape_room.py"
LOG_FILE="/home/$USER/Smart-Home-Escape-Room-Workshop/start_node_red.log"
SELENIUM_PROCESS="selenium-server"
SELENIUM_COMMAND="java -jar /usr/local/bin/selenium-server-4.27.0.jar standalone"

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

# Prüfen, ob openHAB verfügbar ist
function is_openhab_reachable() {
    host="192.168.0.5"
    port=8080
    nc -z -w 2 "$host" "$port"
    return $?
}

# Node-RED starten, wenn es nicht läuft
if is_node_red_running; then
    echo "Node-RED läuft bereits."
else
    echo "Prüfe, ob openHAB verfügbar ist..."
    if is_openhab_reachable; then
        echo "openHAB ist erreichbar. Starte Node-RED..."
        bash "$NODE_RED_SCRIPT" > "$LOG_FILE" 2>&1 &
        sleep 2
        if is_node_red_running; then
            echo "Node-RED erfolgreich gestartet."
        else
            echo "Fehler: Node-RED konnte nicht gestartet werden."
            exit 1
        fi
    else
        echo "openHAB ist nicht erreichbar. Node-RED wird nicht gestartet."
        exit 1
    fi
fi

# Selenium-Server starten, wenn er nicht läuft
if is_selenium_running; then
    echo "Selenium-Server läuft bereits."
else
    echo "Starte Selenium-Server..."
    $SELENIUM_COMMAND > /dev/null 2>&1 &
    sleep 2
    if is_selenium_running; then
        echo "Selenium-Server erfolgreich gestartet."
    else
        echo "Fehler: Selenium-Server konnte nicht gestartet werden."
        exit 1
    fi
fi

# Python-Skript starten
echo "Starte Escape Room..."
python3 "$PYTHON_SCRIPT"
