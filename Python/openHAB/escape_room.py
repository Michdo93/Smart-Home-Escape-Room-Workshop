import core
from core.rules import rule
from core.triggers import when
import threading
import subprocess
import platform
import time
import paramiko

SSH_USERNAME = "michael"
SSH_PASSWORT = "linux"
SSH_TARGET = "192.168.0.218"
SSH_BASE_PATH = "/home/michael/Smart-Home-Escape-Room-Workshop/Python/"

def execute_remote_python_script(username, password, target, python_version, file_path, file):
    if ping_target(target):
        # Wenn der Zielrechner erreichbar ist, SSH-Verbindung herstellen und das Python-Programm ausführen
        try:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(target, username=username, password=password)

            # Befehl auf dem Zielrechner ausführen
            stdin, stdout, stderr = ssh_client.exec_command('{} {}'.format(python_version, file_path + file))

            # Ergebnis abrufen und ausgeben (optional)
            output = stdout.read()
            print(output)

            ssh_client.close()
        except Exception as e:
            print('Fehler bei der SSH-Verbindung oder Ausführung des Skripts:', str(e))
    else:
        print('Zielrechner nicht erreichbar')

def ping_target(host):
    timeout = 5  # 5 Sekunden Timeout
    if platform.system() == "Windows":
        command = ['ping', '-n', '1', host]
    else:
        command = ['ping', '-c', '1', host]

    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        start_time = time.time()

        while True:
            return_code = process.poll()
            if return_code is not None:
                break

            if time.time() - start_time > timeout:
                process.terminate()
                return False

        output = process.stdout.read()

        if "Zielhost nicht erreichbar." in output or "Destination Host Unreachable" in output:
            return False
        return True
    except Exception as e:
        #print("Fehler beim Ausführen des Ping-Befehls:", str(e))
        return False

@rule("Escape Room init")
@when("System started")
def escape_room_init(event):
    items = [
        "EscapeRoomStart",
        "EscapeRoomLevel1",
        "EscapeRoomLevel2",
        "EscapeRoomLevel3",
        "EscapeRoomLevel4",
        "EscapeRoomLevel5",
        "EscapeRoomLevel6",
        "EscapeRoomLevel7",
        "EscapeRoomLevel8",
        "EscapeRoomLevel9",
        "EscapeRoomLevel10",
        "EscapeRoomLevel11",
        "EscapeRoomLevel12",
        "EscapeRoomLevel13",
        "EscapeRoomLevel14",
        "EscapeRoomLevel15",
        "EscapeRoomLevel16",
        "EscapeRoomLevel17",
        "EscapeRoomLevel18",
        "EscapeRoomLevel19",
        "EscapeRoomLevel20"
    ]

    threads = []
    for item in items:
        thread = threading.Thread(target=events.postUpdate, args=(item, "OFF"))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

@rule("Escape Room Starten/Stoppen")
@when("Item EscapeRoomStart received command")
def escape_room_running(event):
    if event.itemCommand == ON:
        execute_remote_python_script("nao", "P3pp3r2!", "192.168.0.42", "/usr/bin/python", "/home/nao/", "escape_room_intro.py")
    else:
        execute_remote_python_script(SSH_USERNAME, SSH_PASSWORT, SSH_TARGET, "/usr/bin/python3", SSH_BASE_PATH + "Laptop/", "stop_escape_room.py")

@rule("Escape Room Level 1")
@when("Item EscapeRoomLevel1 received command")
def escape_room_level(event):
    if event.itemCommand == ON:
        execute_remote_python_script(SSH_USERNAME, SSH_PASSWORT, SSH_TARGET, "/usr/bin/python3", SSH_BASE_PATH + "Laptop/", "automate_escape_room_laptop.py open TXT Multimedia EingabeNumbleLoesung")
    else:
        execute_remote_python_script(SSH_USERNAME, SSH_PASSWORT, SSH_TARGET, "/usr/bin/python3", SSH_BASE_PATH + "Laptop/", "automate_escape_room_laptop.py close TXT Multimedia EingabeNumbleLoesung")

@rule("Escape Room Level 2")
@when("Item EscapeRoomLevel2 received command")
def escape_room_level(event):
    execute_remote_python_script(SSH_USERNAME, SSH_PASSWORT, SSH_TARGET, "/usr/bin/python3", SSH_BASE_PATH + "Laptop/", "automate_escape_room_laptop.py close TXT Multimedia EingabeNumbleLoesung")

    time.sleep(1)

    if event.itemCommand == ON:
        execute_remote_python_script(SSH_USERNAME, SSH_PASSWORT, SSH_TARGET, "/usr/bin/python3", SSH_BASE_PATH + "Laptop/", "automate_escape_room_laptop.py open TXT Multimedia EingabeMorsecode")
    else:
        execute_remote_python_script(SSH_USERNAME, SSH_PASSWORT, SSH_TARGET, "/usr/bin/python3", SSH_BASE_PATH + "Laptop/", "automate_escape_room_laptop.py close TXT Multimedia EingabeMorsecode")
"""
@rule("Escape Room Level 3")
@when("Item EscapeRoomLevel3 received command")
def escape_room_level(event):
    if event.itemCommand == ON:
        events.sendCommand("", "")
"""
@rule("Escape Room Level 4")
@when("Item EscapeRoomLevel4 received command")
def escape_room_level(event):
    if event.itemCommand == ON:
        execute_remote_python_script(SSH_USERNAME, SSH_PASSWORT, SSH_TARGET, "/usr/bin/python3", SSH_BASE_PATH + "Laptop/", "automate_escape_room_laptop.py open HTML IoT ErkennungTotenschaedel")
        execute_remote_python_script(SSH_USERNAME, SSH_PASSWORT, SSH_TARGET, "/usr/bin/python3", SSH_BASE_PATH + "Laptop/", "automate_escape_room_laptop.py open TXT IoT EingabeSchaedel")
    else:
        execute_remote_python_script(SSH_USERNAME, SSH_PASSWORT, SSH_TARGET, "/usr/bin/python3", SSH_BASE_PATH + "Laptop/", "automate_escape_room_laptop.py close TXT IoT EingabeSchaedel")
        execute_remote_python_script(SSH_USERNAME, SSH_PASSWORT, SSH_TARGET, "/usr/bin/python3", SSH_BASE_PATH + "Laptop/", "automate_escape_room_laptop.py close HTML IoT ErkennungTotenschaedel")

@rule("Escape Room Level 5")
@when("Item EscapeRoomLevel5 received command")
def escape_room_level(event):
    execute_remote_python_script(SSH_USERNAME, SSH_PASSWORT, SSH_TARGET, "/usr/bin/python3", SSH_BASE_PATH + "Laptop/", "automate_escape_room_laptop.py close TXT IoT EingabeSchaedel")
    execute_remote_python_script(SSH_USERNAME, SSH_PASSWORT, SSH_TARGET, "/usr/bin/python3", SSH_BASE_PATH + "Laptop/", "automate_escape_room_laptop.py close HTML IoT ErkennungTotenschaedel")

    time.sleep(1)

    if event.itemCommand == ON:
        execute_remote_python_script(SSH_USERNAME, SSH_PASSWORT, SSH_TARGET, "/usr/bin/python3", SSH_BASE_PATH + "Laptop/", "automate_escape_room_laptop.py open HTML IoT ErkennungPosen")
        execute_remote_python_script(SSH_USERNAME, SSH_PASSWORT, SSH_TARGET, "/usr/bin/python3", SSH_BASE_PATH + "Laptop/", "automate_escape_room_laptop.py open TXT IoT EingabeMordtat")
    else:
        execute_remote_python_script(SSH_USERNAME, SSH_PASSWORT, SSH_TARGET, "/usr/bin/python3", SSH_BASE_PATH + "Laptop/", "automate_escape_room_laptop.py close TXT IoT EingabeMordtat")
        execute_remote_python_script(SSH_USERNAME, SSH_PASSWORT, SSH_TARGET, "/usr/bin/python3", SSH_BASE_PATH + "Laptop/", "automate_escape_room_laptop.py close HTML IoT ErkennungPosen")

"""
@rule("Escape Room Level 6")
@when("Item EscapeRoomLevel6 received command")
def escape_room_level(event):
    if event.itemCommand == ON:
        events.sendCommand("", "")

@rule("Escape Room Level 7")
@when("Item EscapeRoomLevel7 received command")
def escape_room_level(event):
    if event.itemCommand == ON:
        events.sendCommand("", "")

@rule("Escape Room Level 8")
@when("Item EscapeRoomLevel8 received command")
def escape_room_level(event):
    if event.itemCommand == ON:
        events.sendCommand("", "")

@rule("Escape Room Level 9")
@when("Item EscapeRoomLevel9 received command")
def escape_room_level(event):
    if event.itemCommand == ON:
        events.sendCommand("", "")

@rule("Escape Room Level 10")
@when("Item EscapeRoomLevel10 received command")
def escape_room_level(event):
    if event.itemCommand == ON:
        events.sendCommand("", "")

@rule("Escape Room Level 11")
@when("Item EscapeRoomLevel11 received command")
def escape_room_level(event):
    if event.itemCommand == ON:
        events.sendCommand("", "")

@rule("Escape Room Level 12")
@when("Item EscapeRoomLevel12 received command")
def escape_room_level(event):
    if event.itemCommand == ON:
        events.sendCommand("", "")

@rule("Escape Room Level 13")
@when("Item EscapeRoomLevel13 received command")
def escape_room_level(event):
    if event.itemCommand == ON:
        events.sendCommand("", "")

@rule("Escape Room Level 14")
@when("Item EscapeRoomLevel14 received command")
def escape_room_level(event):
    if event.itemCommand == ON:
        events.sendCommand("", "")

@rule("Escape Room Level 15")
@when("Item EscapeRoomLevel15 received command")
def escape_room_level(event):
    if event.itemCommand == ON:
        events.sendCommand("", "")

@rule("Escape Room Level 16")
@when("Item EscapeRoomLevel1 received command")
def escape_room_level(event):
    if event.itemCommand == ON:
        events.sendCommand("", "")

@rule("Escape Room Level 16")
@when("Item EscapeRoomLevel1 received command")
def escape_room_level(event):
    if event.itemCommand == ON:
        events.sendCommand("", "")

@rule("Escape Room Level 17")
@when("Item EscapeRoomLevel17 received command")
def escape_room_level(event):
    if event.itemCommand == ON:
        events.sendCommand("", "")

@rule("Escape Room Level 18")
@when("Item EscapeRoomLevel18 received command")
def escape_room_level(event):
    if event.itemCommand == ON:
        events.sendCommand("", "")

@rule("Escape Room Level 19")
@when("Item EscapeRoomLevel19 received command")
def escape_room_level(event):
    if event.itemCommand == ON:
        events.sendCommand("", "")

@rule("Escape Room Level 20")
@when("Item EscapeRoomLevel20 received command")
def escape_room_level(event):
    if event.itemCommand == ON:
        events.sendCommand("", "")
"""