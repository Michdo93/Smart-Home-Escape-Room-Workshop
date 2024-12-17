#!/bin/bash

# Desktop-Verzeichnis des aktuellen Benutzers
DESKTOP_DIR="$HOME/Schreibtisch"
if [ ! -d "$DESKTOP_DIR" ]; then
  DESKTOP_DIR="$HOME/Desktop"
fi

# Überprüfen, ob Desktop-Verzeichnis existiert
if [ ! -d "$DESKTOP_DIR" ]; then
  echo "Fehler: Desktop-Verzeichnis nicht gefunden."
  exit 1
fi

# Pfade zu den Skripten und Icons
START_SCRIPT="$HOME/Smart-Home-Escape-Room-Workshop/start_escape_room.sh"
STOP_SCRIPT="$HOME/Smart-Home-Escape-Room-Workshop/stop_escape_room.sh"
START_ICON="$HOME/Smart-Home-Escape-Room-Workshop/start_escape_room.png"
STOP_ICON="$HOME/Smart-Home-Escape-Room-Workshop/stop_escape_room.png"

# Start Desktop Entry
cat <<EOF > "$DESKTOP_DIR/start_escape_room.desktop"
[Desktop Entry]
Type=Application
Name=Escape Room starten
Exec=bash "$START_SCRIPT"
Terminal=false
Icon=$START_ICON
StartupNotify=false
EOF

# Stop Desktop Entry
cat <<EOF > "$DESKTOP_DIR/stop_escape_room.desktop"
[Desktop Entry]
Type=Application
Name=Escape Room beenden
Exec=bash "$STOP_SCRIPT"
Terminal=false
Icon=$STOP_ICON
StartupNotify=false
EOF

# Sicherstellen, dass die Dateien ausführbar sind
chmod +x "$DESKTOP_DIR/start_escape_room.desktop"
chmod +x "$DESKTOP_DIR/stop_escape_room.desktop"

echo "Desktop-Einträge erstellt und nach $DESKTOP_DIR kopiert."

# Pfad zur flows.json
FLOW_FILE="./EscapeRoom/Technik/flows.json"

# Überprüfen, ob die flows.json existiert
if [ ! -f "$FLOW_FILE" ]; then
  echo "Fehler: $FLOW_FILE nicht gefunden."
  exit 1
fi

# $USER in der flows.json ersetzen
sed -i "s|\\\$USER|$USER|g" "$FLOW_FILE"

echo "flows.json erfolgreich aktualisiert: $FLOW_FILE"
