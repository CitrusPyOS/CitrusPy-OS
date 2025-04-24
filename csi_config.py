import json
import os

with open("csi.json", "r") as file:
    data = json.load(file)

    emergency_password = data['emergency_password']

def csi_config():
    os.system('cls')

    print("CSI Configuration v.prototype0.0.1")
    print("__________________________________")
    print("                                  ")
    print("1. Manage emergency password")
    print("2. Manage tracking (INCOMPLETE DO NOT SELECT)")

    user_input = input("Choose an option. ")
    if user_input == "1":
        with open("csi.json", "r") as file:
            data = json.load(file)
        user_input = input(f"The emergency password is '{data['emergency_password']}'. Change? (Y/N) ")
        if user_input == "y" or user_input == "yes":
            emergency_password = input("Set a new password: ")
            data['emergency_password'] = emergency_password
            with open("csi.json", 'w') as file:
                json.dump(data, file, indent=4)

            print("Password updated successfully.")
            user_input = input("Press enter to return.")
            with open('user_input.py') as file:
                exec(file.read())
    if user_input == "2":
        print("1. Enable tracking of failed logins on admins")
        print("2. Enable tracking of failed attempts to access the emergency settings")
        print("3. View user accounts")
    else:
        with open('user_input.py') as file:
                         exec(file.read())
csi_config()