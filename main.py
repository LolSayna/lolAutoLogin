import time
import os
import sys
import subprocess

from pynput.keyboard import Key, Controller
keyboard = Controller()

# the main launch process
def launch(username, password, path):

    subprocess.call([path])

    time.sleep(2)

    keyboard.type(username)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(0.25)
    keyboard.type(password)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    
    
print("Starting Auto-login!")

# checking wether als arguments are given
if len(sys.argv) != 4:

    print("Wrong syntax call, required is:\nACCOUNTNAME PASSWORD FULL_PATH_TO_LeagueClient.exe")
    time.sleep(10)

# check if lol client is already runnning
progs = str(subprocess.check_output('tasklist'))
if "LeagueClient.exe" in progs:

    print("Running Client found, closing...")
    os.system('taskkill /f /im LeagueClient.exe')

# login
print(f"Logging into {sys.argv[1]}.")
launch(sys.argv[1], sys.argv[2], sys.argv[3])
