import os
import pyautogui
import time
from PyChromeController import PyChromeController

pyautogui.FAILSAFE = False

BASE_PATH = "/home/michael/Smart-Home-Escape-Room-Workshop/Python/Laptop/"

def stop_escape_room():
    pid_file = "EscapeRoom.lock"

    controller = PyChromeController()
    url = "http://localhost:1880/"

    if os.path.isfile(BASE_PATH + pid_file):
        with open(BASE_PATH + pid_file, 'r') as read_pid:
            session_id = read_pid.read().strip()

            controller.attach_browser_session(session_id)
            # Fenster maximieren
            controller.maximize_window()

            controller.switch_tab_by_url(url)
    else:        
        controller.start_browser_session()
        controller.open_url(url)

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

    controller.close_browser()

    os.remove(BASE_PATH + pid_file)

if __name__ == "__main__":
    stop_escape_room()
