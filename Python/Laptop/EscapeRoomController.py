#!/usr/bin/env python3
import os
import sys
import pyautogui
import time
from PyChromeController import PyChromeController

class EscapeRoomController:
    def __init__(self, base_path=None):
        self.base_path = os.path.expanduser(base_path or "~/Smart-Home-Escape-Room-Workshop/Python/Laptop/")
        self.pid_path = os.path.join(self.base_path, "PID")
        self.controller = PyChromeController()
        self.url = "http://localhost:1880/"
        pyautogui.FAILSAFE = False

    def is_running(self, pid_file):
        """Überprüft, ob eine PID-Datei existiert."""
        pid_path = os.path.join(self.pid_path, pid_file)
        print(f"Prüfe auf Datei: {pid_path}")
        return os.path.isfile(pid_path)

    def save_session_id(self, pid_file):
        """Speichert die Session ID in die PID-Datei."""
        if self.controller:
            session_id = self.controller.driver.session_id
            pid_path = os.path.join(self.pid_path, pid_file)
            with open(pid_path, 'w') as write_pid:
                write_pid.write(session_id)

    def load_session_id(self, pid_file):
        """Lädt die Session ID aus der PID-Datei."""
        pid_path = os.path.join(self.pid_path, pid_file)

        if os.path.isfile(pid_path):
            with open(pid_path, 'r') as read_pid:
                session_id = read_pid.read().strip()
            return session_id
        return None

    def start_browser(self):
        """Startet den Browser und öffnet die erforderliche URL."""
        self.controller.start_browser_session()
        self.controller.open_url(self.url)
        time.sleep(3)

    def stop_browser(self, pid_file):
        """Schließt den Browser und löscht die PID-Datei."""
        self.controller.close_browser()
        pid_path = os.path.join(self.pid_path, pid_file)
        if os.path.isfile(pid_path):
            os.remove(pid_path)

    def find_and_click_button(self, button_image, confidence=0.85):
        """Sucht ein Button-Bild auf dem Bildschirm und klickt es."""
        button_path = os.path.join(self.base_path, button_image)

        while True:
            try:
                button = pyautogui.locateOnScreen(button_path, confidence=confidence)
                if button is not None:
                    center_x, center_y = pyautogui.center(button)
                    left_x = center_x - (button.width / 2) + 30
                    pyautogui.click(left_x, center_y)
                    break
            except Exception as e:
                print(e)
            time.sleep(0.3)

    def flow_to_fix(self):
        """Führt den Flow-to-Fix-Prozess aus."""
        pid_file = "FlowToFix.lock"

        if self.is_running(pid_file):
            print("Flow to Fix läuft bereits!")
            return

        # Starten oder an bestehende Sitzung anknüpfen
        session_id = self.load_session_id("EscapeRoom.lock")
        if session_id:
            self.controller.attach_browser_session(session_id)
            self.controller.maximize_window()
            self.controller.check_and_open_tab_by_url(self.url)
        else:
            self.start_browser()

        time.sleep(3)
        self.find_and_click_button("FlowToFix.png", confidence=0.95)
        self.save_session_id(pid_file)

    def start_escape_room(self):
        """Startet den Escape Room."""
        if self.is_running("EscapeRoom.lock"):
            print("Der Escape Room wird bereits ausgeführt!")
            return

        self.start_browser()
        self.find_and_click_button("EscapeRoom_Starten.png")
        self.controller.minimize_window()
        self.save_session_id("EscapeRoom.lock")

    def stop_escape_room(self):
        """Beendet den Escape Room."""
        session_id = self.load_session_id("EscapeRoom.lock")

        if session_id:
            self.controller.attach_browser_session(session_id)
            self.controller.maximize_window()
            self.controller.switch_tab_by_url(self.url)
        else:
            self.start_browser()

        self.find_and_click_button("EscapeRoom_Beenden.png")
        time.sleep(3)
        self.stop_browser("EscapeRoom.lock")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Verwendung: python3 EscapeRoomController.py <start/stop/fix>")
    else:
        action = sys.argv[1].lower()

        controller = EscapeRoomController()
        
        if action == "start":
            controller.start_escape_room()
        elif action == "stop":
            controller.stop_escape_room()
        elif action == "fix":
            controller.flow_to_fix()
        else:
            print("Ungültige Eingabe. Bitte geben Sie 'start', 'stop' oder 'fix' ein.")
