import subprocess
import signal
import sys
import os
from PyChromeController import PyChromeController
from selenium import webdriver

ESCAPE_ROOM_BASE_PATH = '/home/michael/Smart-Home-Escape-Room-Workshop'

PID_FILE_PATH = ESCAPE_ROOM_BASE_PATH + '/Python/Laptop/PID'

ROOM1_BASE_PATH = ESCAPE_ROOM_BASE_PATH + '/EscapeRoom/Workshop Dateien/Raum 1/Laptop Dateien'
ROOM2_BASE_PATH = ESCAPE_ROOM_BASE_PATH + '/EscapeRoom/Workshop Dateien/Raum 2/Laptop Dateien'
ROOM3_BASE_PATH = ESCAPE_ROOM_BASE_PATH + '/EscapeRoom/Workshop Dateien/Raum 3/Magic Mirror Dateien'
ROOM4_BASE_PATH = ESCAPE_ROOM_BASE_PATH + ''
ROOM5_BASE_PATH = ESCAPE_ROOM_BASE_PATH + ''

ROOM1_FILES = {
    "EingabeMorsecode": "morseinput.txt",
    "EingabeNumbleLoesung": "numble.txt",
    "TagebucheintragReise": "Tagebucheintrag_Reise.zip",
    "TagebuchMorsecode": "Tagebuch_Morsecode.zip",
    "Weltuhr": "Weltuhr.zip"
}

ROOM2_FILES = {
    "HinweisAufgabeMordtat": "HinweisAufgabeMordtat.txt",
    "EingabeMordtat": "mordtat.txt",
    "EingabeSchaedel": "schaedel.txt",
    "ErkennungPosen": "https://teachablemachine.withgoogle.com/models/ANbjKGJ5D/",
    "ErkennungTotenschaedel": "https://teachablemachine.withgoogle.com/models/Icw7c4jZE/"
}

ROOM3_FILES = {
    "Abschlussquiz": "abschlussquiz.zip",
    "Zeitungsartikel": "Zeitungsartikel+Forschungsprojekt.png",
    "": "",
    "": "",
}

ROOM4_FILES = {
    "": "",
    "": "",
    "": "",
    "": "",
}

ROOM5_FILES = {
    "": "",
    "": "",
    "": "",
    "": "",
}

ROOM1_SYNONYMS = ["room1", "room one", "Raum 1", "Raum eins", "Multimedia", "Multimediaraum", "Multimediazimmer"]
ROOM2_SYNONYMS = ["room2", "room two", "Raum 2", "Raum zwei", "IoT", "IoT-Raum", "IoT-Zimmer"]
ROOM3_SYNONYMS = ["room3", "room three", "Raum 3", "Raum drei", "Bad", "Badezimmer"]
ROOM4_SYNONYMS = ["room4", "room four", "Raum 4", "Raum 4", "Küche"]
ROOM5_SYNONYMS = ["room5", "room five", "Raum 5", "Raum 5", "Konferenz", "Konferenzraum", "Konferenzzimmer"]

def check_synonyms(input_string, synonym_list):
    for synonym in synonym_list:
        if synonym in input_string:
            return True
    return False

def getFilenameByFile(room, file):
    if check_synonyms(room, ROOM1_SYNONYMS):
        files_list = ROOM1_FILES
    elif check_synonyms(room, ROOM2_SYNONYMS):
        files_list = ROOM2_FILES
    elif check_synonyms(room, ROOM3_SYNONYMS):
        files_list = ROOM3_FILES
    elif check_synonyms(room, ROOM4_SYNONYMS):
        files_list = ROOM4_FILES
    elif check_synonyms(room, ROOM5_SYNONYMS):
        files_list = ROOM5_FILES
    else:
        return ""
    
    for filekey, filename in files_list.items():
        if file == filekey:
            return filename
    return ""

def getPathByRoom(room):
    if check_synonyms(room, ROOM1_SYNONYMS):
        return ROOM1_BASE_PATH + "/"
    elif check_synonyms(room, ROOM2_SYNONYMS):
        return ROOM2_BASE_PATH + "/"
    elif check_synonyms(room, ROOM3_SYNONYMS):
        return ROOM3_BASE_PATH + "/"
    elif check_synonyms(room, ROOM4_SYNONYMS):
        return ROOM4_BASE_PATH + "/"
    elif check_synonyms(room, ROOM5_SYNONYMS):
        return ROOM5_BASE_PATH + "/"
    return ""

def open_file(file_type, room, file):
    if getFilenameByFile(room, file) != "":
        filename = getFilenameByFile(room, file)
    else:
        print(f"Für die Datei {file} konnte kein Dateiname gefunden werden!")
        return

    if getPathByRoom(room) != "":
        path = getPathByRoom(room)
    else:
        print(f"Für den Raum {room} konnte auf diesem System kein Pfad gefunden werden!")
        return

    if "http" not in filename:
        file_path = os.path.join(path, filename)

        pid_file = filename.split(".")[0] + "_process.lock"

        if os.path.isfile(PID_FILE_PATH + "/" + pid_file):
            print(f"Die Anwendung für die Datei {filename} läuft bereits und wird durch {pid_file} gelockt!")
            return
    else:
        pid_file = "EscapeRoom.lock"

    try:
        if file_type == "ZIP":
            app_process = subprocess.Popen(['file-roller', file_path])
        elif file_type == "PDF":
            app_process = subprocess.Popen(['evince', file_path])
        elif file_type == "HTML":
            controller = PyChromeController()
            session_id = None

            if os.path.isfile(PID_FILE_PATH + "/" + pid_file):
                with open(PID_FILE_PATH + "/" + pid_file, "r") as file:
                    session_id = file.read().strip()

            if session_id:
                controller.attach_browser_session(session_id)
                controller.maximize_window()
                controller.check_and_open(filename)
            else:
                controller.start_browser_session()
                controller.open_url(filename)

                # Sitzungs-ID speichern
                with open(PID_FILE_PATH + "/" + pid_file, "w") as file:
                    file.write(controller.driver.session_id)
        elif file_type == "PNG":
            app_process = subprocess.Popen(['eog', file_path])
        elif file_type == "TXT":
            app_process = subprocess.Popen(['gedit', '--new-window', file_path])
        elif file_type == "PY":
            app_process = subprocess.Popen(['python3', file_path])
    except FileNotFoundError:
        print(f"{file_type} konnte auf diesem System nicht gefunden werden.")
    except Exception as e:
        print(f"Fehler beim Öffnen der {file_type}-Datei: {str(e)}.")

    if "http" not in filename:
        with open(PID_FILE_PATH + "/" + pid_file, 'w') as write_pid:
            write_pid.write(str(app_process.pid))

def close_file(file_type, room, file):
    if getFilenameByFile(room, file) != "":
        filename = getFilenameByFile(room, file)
    else:
        print(f"Für die Datei {file} konnte kein Dateiname gefunden werden!")
        return

    if "http" not in filename:
        pid_file = filename.split(".")[0] + "_process.lock"

        if os.path.isfile(PID_FILE_PATH + "/" + pid_file):
            with open(PID_FILE_PATH + "/" + pid_file, 'r') as read_pid:
                pid = int(read_pid.read())
            
            try:
                os.kill(pid, signal.SIGTERM)
            except ProcessLookupError:
                print(f"Der Prozess mit der PID {pid} wurde nicht gefunden")
            except Exception as e:
                print(f"Fehler Beenden des Prozesses: {str(e)}.")

            os.remove(PID_FILE_PATH + "/" + pid_file)
        else:
            print(f"Die Lock-Datei {pid_file} für die Datei {filename} konnte nicht gefunden werden. Dies bedeutet, dass die Anwendung nicht läuft bzw. schon beendet wurde.")
    else:
        pid_file = "EscapeRoom.lock"
        controller = PyChromeController()
        session_id = None

        if os.path.isfile(PID_FILE_PATH + "/" + pid_file):
            with open(PID_FILE_PATH + "/" + pid_file, "r") as file:
                session_id = file.read().strip()

        if session_id:
            controller.attach_browser_session(session_id)
            controller.maximize_window()

            if len(controller.driver.window_handles) > 1:
                controller.close_tab_by_url(filename)
                controller.minimize_window()
            else:
                controller.close_browser()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Verwendung: python3 automate_escape_room_laptop.py <open/close> <filetype> <room> <filename>")
    else:
        action = sys.argv[1].lower()
        file_type = sys.argv[2].upper()
        room = sys.argv[3]
        filename = sys.argv[4]

        if action == "open":
            open_file(file_type, room, filename)
        elif action == "close":
            close_file(file_type, room, filename)
