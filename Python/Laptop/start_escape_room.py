#!/usr/bin/env python3
import os
import pyautogui
import time
from PyChromeController import PyChromeController

pyautogui.FAILSAFE = False

BASE_PATH = os.path.expanduser("~/Smart-Home-Escape-Room-Workshop/Python/Laptop/")

def start_escape_room():
    pid_file = "EscapeRoom.lock"

    print(f"Prüfe auf Datei: {BASE_PATH + 'PID/' + pid_file}")

    if os.path.isfile(BASE_PATH + "PID/" + pid_file):
        print("Der Escape Room wird bereits ausgeführt!")
        return
    else:
        # PyChromeController initialisieren
        controller = PyChromeController()

        controller.start_browser_session()
        # Browser starten und Tab öffnen
        controller.open_url("http://localhost:1880/")

        time.sleep(3)

        starten_png_left = None
        while starten_png_left == None:
            try:
                starten_png = pyautogui.locateOnScreen(BASE_PATH + "EscapeRoom_Starten.png", confidence=0.85)
            except Exception as e:
                print(e)

            if starten_png is not None:
                center_x, center_y = pyautogui.center(starten_png)
                left_x = center_x - (starten_png.width / 2) + 30
                pyautogui.click(left_x, center_y)
                break
            time.sleep(0.3)

        # Minimieren des Browserfensters
        controller.minimize_window()
        
        # Session ID speichern (automatisch von der Bibliothek verwaltet)
        session_id = controller.driver.session_id

        with open(BASE_PATH + "PID/" + pid_file, 'w') as write_pid:
            write_pid.write(session_id)

if __name__ == "__main__":
    start_escape_room()
