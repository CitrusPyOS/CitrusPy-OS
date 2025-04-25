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

import os
import json



def syscon():

    os.system('cls' if os.name == 'nt' else 'clear')

    print("System Configuration")

    account_type = "admin"

    if account_type == "standard_user":
        print("You are logged in using a standard account, meaning you may not be able to change or access all settings.")

    print("\nChoose a option.")
    print("")
    print("Manage custom commands")

    print("-------------------------")
    print("")
    print("1. Add objects to List of commands")
    print("2. Delete objects from List of commands")
    print("")
    print("Manage system information")
    print("-------------------------")
    print("")
    print("3. Change region")
    print("")
    print("Manage autoboot")
    print("-------------------------")
    print("")
    print("4. Set a file or program to autoboot")

    try:
        with open("objects.json", "r") as json_file:
            objects = json.load(json_file)

            if not isinstance(objects, list):
                raise ValueError("JSON data is not a list.")
    except (FileNotFoundError, ValueError):
        objects = []
        print("No valid file found. Starting fresh!")

    if objects:
        print("\nCurrent objects in the file:")
        for index, obj in enumerate(objects, start=1):
            if isinstance(obj, dict):
                print(f"{index}. ({obj['command']}): {obj['description']}")
            else:
                print("Invalid object format in the file.")
    else:
        print("\nNo objects found in the file.")

    user_input = input("\nChoose an option: ")
    if user_input == "1":
        access_command = input("Enter the access command for the object: ")
        description = input("Enter the description for the object: ")

        new_object = {
            "command": access_command,
            "description": description
        }
        objects.append(new_object)

        with open("objects.json", "w") as json_file:
            json.dump(objects, json_file, indent=4)
            print("\nObjects have been updated and saved to 'objects.json'.")
        print("\nUpdated objects in the file:")
        for obj in objects:
            print(f"-({obj['command']}): {obj['description']}")
            syscon()
    elif user_input == "2":
        if not objects:
            print("No objects to delete.")
        else:
            print("\nChoose an object to delete:")
            for index, obj in enumerate(objects, start=1):
                print(f"{index}. ({obj['command']}): {obj['description']}")

            try:
                delete_index = int(input("Enter the number of the object to delete: "))
                if 1 <= delete_index <= len(objects):
                    deleted_object = objects.pop(delete_index - 1)
                    print(f"\nDeleted object: ({deleted_object['command']}): {deleted_object['description']}")

                    with open("objects.json", "w") as json_file:
                        json.dump(objects, json_file, indent=4)
                        print("\nObjects have been updated and saved to 'objects.json'.")
                else:
                    print("\nInvalid selection. No object deleted.")
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")
    else:
        if user_input == "3":
               def set_region():

                print("1. North America")
                print("2. European Union")
                print("3. Non EU Europe")
                print("4. Middle East and North Africa")
                print("5. Africa")
                print("6. South America")
                print("7. Asia")
                print("8. Oceania")
                print("9. PWAIS")

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

                                                if region == "9":
                                                    region = "pwais"

                                                else:
                                                    user_input = ("Critical error: Region not supported. xc00938 Please press (Enter) to retry.")
                                                    set_region()

                with open("system_info.json", "r") as file2:
                    data2 = json.load(file2)

                    data2["region"] = region

                    with open("system_info.json", "w") as file2:
                        json.dump(data2, file2, indent=4)
               set_region()


        elif user_input == "4":
                autoboot = input("Enter the path of a file to automatically start after boot: ")
                with open("system_info.json", "r") as file2:
                            data2 = json.load(file2)

                            data2["autoboot"] = autoboot

                            with open("system_info.json", "w") as file2:
                                json.dump(data2, file2, indent=4)


    print("\nInvalid option selected.")
    syscon()

syscon()