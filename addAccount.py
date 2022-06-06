
# Use in terminal for each account.

print("\nCreating .bat file with account credentials.")
print("Example for file name\t: aramAcc")
print("Example for lol path\t: C:\Riot Games\League of Legends\LeagueClient.exe")
print("Example for location\t: C:\\Users\YOUR-NAME\Desktop\lolAutoLogin\main.py\n")

username = input("Enter lol username\t: ")
password = input("Enter lol password\t: ")
filename = input("Enter name for bat file\t: ")
lolPath = input("Enter path of LeagueClient.exe\t: ")
location = input("Enter location of main.py\t: ")

# file extension fix
if not filename.endswith(".bat"):

    filename += ".bat"

# creating and writing into the file
with open(filename, "w") as f:

    # the bat file starts cmd and then the main.py file 
    f.write(f"start cmd /C python {location} {username} {password} \"{lolPath}\"")
    
print(f"Created: \"{filename}\" at: \"{location}\"")