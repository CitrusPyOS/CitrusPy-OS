# Copyright (C) 2025 7908Studios
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/gpl-3.0.html>.


import json

import time

import os

logged_in = "false"

with open("login_temp.json", "w") as f:
                    json.dump({
                        "username": "default",
                        "account_type": "default",
                        "logged_in": "false"
                    }, f, indent=4)

new_user_name = "default"

data = "default"


with open("users.json", "r") as file:
    users = json.load(file)

with open("messages.json", "r") as file:
    messages = json.load(file)

with open("objects.json", "r") as file:
    objects = json.load(file)

with open("csi.json", "r") as file:
    data = json.load(file)

    emergency_password = data['emergency_password']

    def restore_csi():

        file_path = 'csi.json'

        if os.path.exists(file_path):
            print(f"CSI.json file existence confirmed")
        else:
            print(f"Critical error: No CSI.json file found. Please manually manipulate.")    

    def emergency():
        user_input = input("Please contact an administrator to enter the emergency password. ")

        if user_input == emergency_password:

            print("Access granted.")

            print("1. Create a new account with administrator privileges.")

            print("2. Restore CSI file")

            user_input = input("Choose an option. ")

            if user_input == "1":

                new_user_name = input("Please set a username. ")

                data = {"username": new_user_name, "password": "default", "account_type": "admin"}

                try:
                    with open("users.json", "r") as file:
                         users = json.load(file) 
                except FileNotFoundError:
                        users = [] 


                users.append(data)

             
                with open("users.json", "w") as file:
                        json.dump(users, file, indent=4)

                print("Data saved to file.")

                print("Please log in and set a password.")

            if user_input == "2":
                restore_csi()    

        else:
         print("Access denied. Please retry or close the program.")
         emergency()

file_path = 'csi.json'

if os.path.exists(file_path):
    print("System check completed.")
else:
    print("Critical error cx01_000356. Program can not start.")
    user_input = input("Enter (emergency) to access emergency settings.")
    if user_input == emergency:
        emergency()

banned_users = ["benamin15"]

user_found = False

password = "default"

os.system('cls')



 ##################################################
def command_line():


    user_input = input("Choose a task to perform. (list) for a list of commands. (exit) to close program. ")

    if user_input == "create_account":
            with open("login_temp.json", "r") as f:
                data = json.load(f)
                account_type = data["account_type"]
            if account_type == "admin" or account_type == "master_admin":
                new_user_name = input("Please set a username. ")

                data = {"username": new_user_name, "password": "default", "account_type": "standard_user"}

                try:
                    with open("users.json", "r") as file:
                        users = json.load(file) 
                except FileNotFoundError:
                    users = [] 

        
                users.append(data)

        
                with open("users.json", "w") as file:
                    json.dump(users, file, indent=4)

                print("Data saved to file.")

                print("Please log in and set a password.")
                command_line()
            else:
             print("You do not currently process administrator priviliges.")
            command_line()


    if user_input == "debug":
        with open("users.json", "r") as file:
            users = json.load(file)

            with open("login_temp.json", "r") as f:
                data = json.load(f)
                account_type = data["account_type"]

            with open("login_temp.json", "r") as f:
                data = json.load(f)
                username = data["username"]

            with open("login_temp.json", "r") as f:
                data = json.load(f)
                logged_in = data["logged_in"]
        print(f"Account type {account_type}")
        print(f"Logged in? {logged_in}")
        print(f"Username {username}")
        print(users)
        command_line()
        

    if user_input == "list":
        print("-(messenger): Messaging tool")
        print("-(csi_config): Configure CSI-Information")
        print("-(create_account): Create a local user account")
        print("-(run): Access a specific file")
        print("-(start_program): Start a .py program")
        print("-(syscon): System configuration")
        print("-(change_pass): Change the password of your account")
        print("-(delete_account): Delete your user account")
        print("-(sysver): See the version of the OS")
        print("-(browser): Access the telecommunications network")
        print("-(AER): Line based text editor")
        print("-(+writer): GUI-Based Text Editor")
        print("-(videogames): Play Video Games")
        with open('objects.json', 'r') as file:
         objects = json.load(file)
         for obj in objects:
            print(f"-({obj["command"]}): {obj["description"]}")
            


    else:
    
        if user_input == "messenger":
            user_input2 = input("Enter (read) to access your messages. Enter (send) to send a message: ")

            if user_input2 == "read":
                try:
                    with open("messages.json", "r") as messages_file:
                        messages = json.load(messages_file)
                        with open("login_temp.json", "r") as f:
                                        data3 = json.load(f)
                                        username = data3["username"]
                        for message in messages:
                            if username == message["user"]: 
                                print(f"Message by {message['sender']}: {message['content']}")
                except FileNotFoundError:
                    print("No messages yet.")
                except json.JSONDecodeError:
                    print("Error reading messages.")

            if user_input2 == "send":
                send_to_user = input("Send to which user? ")
                message = input("Write your message: ")
                with open("login_temp.json", "r") as f:
                 data3 = json.load(f)
                username = data3["username"]
                data = {"user": send_to_user, "content": message, "sender": username}

                try:
                    with open("messages.json", "r") as file:
                        messages = json.load(file)
                except (FileNotFoundError, json.JSONDecodeError):
                    messages = []

                messages.append(data)

                with open("messages.json", "w") as file:
                    json.dump(messages, file, indent=4)



    if user_input == "csi_config" or user_input == "csi_configuration":
        with open('csi_config.py') as file:
            exec(file.read())

    if user_input == "run":
        run = input("Enter a file to access. ")
        file_path = run

        if os.path.exists(file_path):
            print(f"File existence confirmed. Executing")
            with open(run) as file:
                exec(file.read())
        else:
            print(f"File not found. Press enter to return.")
            command_line()


    if user_input == "syscon":
        import subprocess
        subprocess.run(["python", "syscon.py"])

    if user_input == "browser":
        import subprocess
        subprocess.run(["python", "browser.py"])


    if user_input == "+writer":
        import subprocess
        subprocess.run(["python", "+writer.py"])


    if user_input == "start_program":
            run = input("Enter a program to access. ")
            file_path = run

            if os.path.exists(file_path):
                print(f"File existence confirmed. Executing")
                import subprocess
                subprocess.run(["python", run])

            else:
                print(f"File not found. Press enter to return.")
                command_line()


    if user_input == "activate":
        with open('activation.py') as file:
            exec(file.read())

    if user_input == "calc":
        import subprocess
        subprocess.run(["python", "calc.py"])



    if user_input == "delete_account":
        with open("login_temp.json", "r") as f:
                data = json.load(f)
                username = data["username"]

        with open("users.json", "r") as file:
            users = json.load(file)


        updated_users = [user for user in users if user["username"] != username]

        if len(updated_users) == len(users):
            print("User not found.")
        else:
            print(f"User '{username}' has been deleted.")

            with open("users.json", "w") as file:
                json.dump(updated_users, file, indent=4)

                logged_in = "false"

                with open("login_temp.json", "w") as f:
                                    json.dump({
                                        "username": "default",
                                        "account_type": "default",
                                        "logged_in": "false"
                                    }, f, indent=4)
                
                print("Your account is inusable. Please log off.")


 

    if user_input == "aer":
        user_input = "default"
        import subprocess
        subprocess.run(["python", "aer.py"])

    if user_input == "sysver":
        print("CitrusPy OS")
        print("---------")
        print("")
        print("Current Version: early_prototype_public_demo.1")
        print("All previous versions:")
        print("early_prototype0.01")
        print("early_prototype0.02")
        print("early_prototype0.03")
        command_line()


    if user_input == "change_pass":
        
        new_password = input("Set a new password: ")

        with open("users.json", "r") as file:
            users = json.load(file)
            with open("login_temp.json", "r") as f:
                data3 = json.load(f)
                username = data3["username"]

        for user in users:
            if username == user["username"]:
                user["password"] = new_password
                break
        else:
            print("Username not found.")

        with open("users.json", "w") as file:
            json.dump(users, file, indent=4)
        
        command_line()

    else:
            print("Error: Command or File not found.")
            command_line()
def login():
    user_found = False



    password = "default"
    print("CitrusPy OS                   version: early_prototype_public_demo.1")
    print("____________________________________________________________________")
    print("")
    print("This project is licensed under the GNU General Public License v3.0 (GPLv3).")
    print("© 2025 7908Studios")  
    print("See the LICENSE file for details.")
    print("")
    
    with open("csi.json", "r") as file:
            data = json.load(file)
            if data.get("setup_completed") == "false":
                print('Setup starting.')
                print("Disclaimer! This software is an early prototype with minimum security and is prone to data corruption and deletion. YOUR DATA IS NOT SAFE")
            


                def set_region():

                    print("1. North America")
                    print("2. European Union")
                    print("3. Non EU Europe")
                    print("4. Middle East and North Africa")
                    print("5. Africa")
                    print("6. South America")
                    print("7. Asia")
                    print("8. Oceania")

                    region = input("Please set your region. ")

                    if region == "1":
                        region = "north_america"

                    else:

                        if region == "2":
                            region = "eu"

                        else:

                            if region == "3":
                                region = "north_america"
                                
                            else:

                                if region == "4":
                                    region = "middle_east_north_africa"
                                
                                else:

                                    if region == "5":
                                        region = "africa"

                                    else:

                                        if region == "6":
                                            region = "south_america"

                                        else:

                                            if region == "7":
                                                region = "asia"
                                                
                                            else:

                                                if region == "8":
                                                    region = "oceania"
                                    

                                                else:
                                                    user_input = ("Critical error: Region not supported. xc00938 Please press (Enter) to retry.")
                                                    set_region()

                    with open("system_info.json", "r") as file2:
                        data2 = json.load(file2)

                        data2["region"] = region

                        with open("system_info.json", "w") as file2:
                            json.dump(data2, file2, indent=4)

                set_region()

                new_user_name = input("Please set a username for your new account: ")

                data = {"username": new_user_name, "password": "default", "account_type": "admin"}

                try:
                            with open("users.json", "r") as file:
                                users = json.load(file) 
                except FileNotFoundError:
                                users = [] 


                users.append(data)

                    
                with open("users.json", "w") as file:
                                json.dump(users, file, indent=4)

                print("Data saved to file.")

                print("Please reboot to log in and set a password. Your current password is 'Default'.")

                with open("csi.json", "r") as file:
                    data = json.load(file)

                data["setup_completed"] = "true"

                with open("csi.json", "w") as file:
                    json.dump(data, file, indent=4)
            else:


                username = input("Please enter your username: ")

                if username == "emergency":
                    emergency()

                else:
                    with open("users.json", "r") as file:
                        users = json.load(file)
                        user_found = False
                        for user in users:
                                    if username == user["username"]:
                                        user_found = True
                                        break
                    

                                            

                    if user_found:
                        print("User found")
                        password = input("Please enter your password: ")

                        if password == user["password"]:
                            print("Log in attempt successful.")
                            password_correct = True
                        else:
                            password_correct = False
                            print("Error: The user wasn't found or the password is false.")

                        if password_correct:
                            print(f"Logged in as {username}")
                            with open("login_temp.json", "w") as f:
                                json.dump({
                                    "logged_in": "true"
                                }, f, indent=4)
                            account_type = user["account_type"]

                            with open("login_temp.json", "w") as f:
                                json.dump({
                                    "username": username,
                                    "account_type": account_type,
                                    "logged_in": "true"
                                }, f, indent=4)

                            command_line()
                        else:
                            print("Unable to log in.")
                            login()
                            logged_in = False




with open("system_info.json", "r") as file:
    data = json.load(file)

if data.get("autoboot") != "none":
    user_input = input(f"Starting {data.get("autoboot")}. Press enter to confirm or (abort) to boot normally. ")
    if user_input != "abort":
        import subprocess
        subprocess.run(["python", data.get("autoboot") ])
    else:
         login()

else:
     login()                                                                    


login()

if logged_in == "true":
    command_line()