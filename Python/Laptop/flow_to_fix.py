#!/usr/bin/env python3
import os
import subprocess
import pyautogui
import time

pyautogui.FAILSAFE = False

BASE_PATH = "/home/michael/Smart-Home-Escape-Room-Workshop/Python/Laptop/"

def flow_to_fix():
    pid_file = "FlowToFix.lock"

    if os.path.isfile(BASE_PATH + "PID/" + pid_file):
        print("Der Escape Room wird bereits ausgeführt!")
        return
    else:
        app_process = subprocess.Popen(['firefox', '--new-window', "http://localhost:1880/"])

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
            write_pid.write(str(app_process.pid))

if __name__ == "__main__":
    flow_to_fix()