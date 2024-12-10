#!/usr/bin/env python3
import os
import pyautogui
import time
from PyChromeController import PyChromeController

pyautogui.FAILSAFE = False

BASE_PATH = os.path.expanduser("~/Smart-Home-Escape-Room-Workshop/Python/Laptop/")

def flow_to_fix():
    pid_file = "FlowToFix.lock"

    if os.path.isfile(BASE_PATH + "PID/" + pid_file):
        print("Der Escape Room wird bereits ausgeführt!")
        return
    else:
        controller = PyChromeController()
        url = "http://localhost:1880/"

        if os.path.isfile(BASE_PATH + pid_file):
            with open(BASE_PATH + "EscapeRoom.lock", 'r') as read_pid:
                session_id = read_pid.read().strip()

                controller.attach_browser_session(session_id)
                # Fenster maximieren
                controller.maximize_window()

                controller.check_and_open_tab_by_url("http://localhost:1880/")
        else:        
            controller.start_browser_session()
            controller.open_url(url)

            session_id = controller.driver.session_id

        time.sleep(3)
    
        flow_to_fix_png_left = None
        while flow_to_fix_png_left == None:
            try:
                flow_to_fix_png = pyautogui.locateOnScreen(BASE_PATH + "FlowToFix.png", confidence=0.95)
            except Exception as e:
                print(e)

            if flow_to_fix_png is not None:
                flow_to_fix_center = pyautogui.center(flow_to_fix_png)
                print(flow_to_fix_center)
                pyautogui.click(flow_to_fix_center)
                break
            time.sleep(0.3)

        with open(BASE_PATH + "PID/" + pid_file, 'w') as write_pid:
            write_pid.write(session_id)

if __name__ == "__main__":
    flow_to_fix()
