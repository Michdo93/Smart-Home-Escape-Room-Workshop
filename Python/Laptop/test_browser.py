import subprocess
import time

BASE_PATH = "/home/michael/Smart-Home-Escape-Room-Workshop/Python/Laptop/"

if __name__ == "__main__":
    # Verwendung: python3 automate_escape_room_laptop.py <open/close> <filetype> <room> <filename>
    # open/close
    print("open posen")
    subprocess.Popen(['python3', BASE_PATH + "automate_escape_room_laptop.py", "open", "HTML", "IoT", "ErkennungPosen"])
    time.sleep(5)
    print("close posen")
    subprocess.Popen(['python3', BASE_PATH + "automate_escape_room_laptop.py", "close", "HTML", "IoT", "ErkennungPosen"])
    time.sleep(5)
    print("open skull")
    subprocess.Popen(['python3', BASE_PATH + "automate_escape_room_laptop.py", "open", "HTML", "IoT", "ErkennungTotenschaedel"])
    time.sleep(5)
    print("close skull")
    subprocess.Popen(['python3', BASE_PATH + "automate_escape_room_laptop.py", "close", "HTML", "IoT", "ErkennungTotenschaedel"])
