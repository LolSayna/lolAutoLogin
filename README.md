# lolAutoLogin
A simple Python tool to automatically enter different login credentials for the League of Legends Client. 

It creates windows script files that call [main.py](main.py), which then starts the league client and inserts the credentials. The credentials are stored in each `.bat` file in plain text, so keep this files secure.

## Features
* No need to type login name and password
* Switch directly between multiple accounts
* Automatically stops the client when its already running
* Call the `.bat` files on mouse or keyboard shortcuts
* Make sure `Stay signed in` is disabled!

## How to use
Python and pip needs to be installed, download the project and move into its directory. Afterwards install the requirements with:
```
pip install -r requirements.txt
```
Then use [addAccount.py](addAccount.py) for each account you want to add:
```
python .\addAccount.py
```
You are promted to insert your login data and installation paths, in the end a `.bat` file is created. 

Each file can be added as a different macro in your mouse/keyboard software, for example in **Corsair iCue** goto `Key Assignments -> Launch App -> Select Application to Launch`.

## Credit
Project was inspired by: https://github.com/CasperDoesCoding/account-manager
