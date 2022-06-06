import time
import os
import sys
import subprocess

from pynput.keyboard import Key, Controller
keyboard = Controller()


def launch(name, pw, path):

    subprocess.call([path])

    time.sleep(2)

    keyboard.type(name)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(0.25)
    keyboard.type(pw)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    
           
        
print("Starting Auto-login!")
if len(sys.argv) != 4:
    print("Wrong call syntax, required is:\nACCOUNTNAME PASSWORD FULL_PATH_TO_LeagueClient.exe")

# check if client is already runnning
progs = str(subprocess.check_output('tasklist'))
if "LeagueClient.exe" in progs:
    print("Running Client found, closing...")
    os.system('taskkill /f /im LeagueClient.exe')

print(f"Logging into {sys.argv[1]}.")
launch(sys.argv[1], sys.argv[2], sys.argv[3])
