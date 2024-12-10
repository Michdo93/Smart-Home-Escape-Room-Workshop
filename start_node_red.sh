#!/usr/bin/bash
host="192.168.0.5"
port=8080

nc -z -w 2 "$host" "$port"

if [ $? -eq 0 ]; then
    /home/$USER/.nvm/versions/node/v16.13.2/bin/node-red /home/michael/Smart-Home-Escape-Room-Workshop/EscapeRoom/Technik/flows.json
else
    echo "Die Adresse ist nicht erreichbar."
fi
