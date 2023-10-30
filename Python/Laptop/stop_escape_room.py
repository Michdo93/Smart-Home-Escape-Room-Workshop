import os
import subprocess
import pyautogui
import time

pyautogui.FAILSAFE = False

BASE_PATH = "/home/michael/Smart-Home-Escape-Room-Workshop/Python/Laptop/"

def start_escape_room():
    pid_file = "EscapeRoom.lock"

    if os.path.isfile(BASE_PATH + pid_file):
        with open(BASE_PATH + pid_file, 'r') as read_pid:
            pid = int(read_pid.read())
    else:
        app_process = subprocess.Popen(['firefox', '--new-window', "http://localhost:1880/"])
        pid = app_process.pid

        time.sleep(3)
    
    beenden_png_left = None
    while beenden_png_left == None:
        try:
            beenden_png = pyautogui.locateOnScreen(BASE_PATH + "EscapeRoom_Beenden.png", confidence=0.85)
        except Exception as e:
            print(e)

        if beenden_png is not None:
            center_x, center_y = pyautogui.center(beenden_png)
            left_x = center_x - (beenden_png.width / 2) + 30
            pyautogui.click(left_x, center_y)
            break
        time.sleep(0.3)
    
    time.sleep(3)

    try:
        os.kill(pid, 15)
    except ProcessLookupError:
        print(f"Der Prozess mit der PID {pid} wurde nicht gefunden")
    except Exception as e:
        print(f"Fehler Beenden des Prozesses: {str(e)}.")

    os.remove(BASE_PATH + pid_file)

if __name__ == "__main__":
    start_escape_room()