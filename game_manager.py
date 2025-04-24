import os
import json

def gamemanager():

    os.system('cls' if os.name == 'nt' else 'clear')

    print("Video Game Manager")
    print("------------------")

    print("A. Add a game")
    print("B. Remove an entry")
    print("C. Run a game")

    try:
            with open("gamelist.json", "r") as json_file:
                games = json.load(json_file)

                if not isinstance(games, list):
                    raise ValueError("JSON data is not a list.")
    except (FileNotFoundError, ValueError):
            games = []
            print("No valid file found.")

    if games:
            for index, game in enumerate(games, start=1):
                if isinstance(game, dict):
                    print(f"{index}. ({game['command']}): {game['description']}")
                else:
                    print("Invalid object format in the file.")
    else:
            print("\nNo objects found in the file.")

    user_input = input("Select an option. ")



    if user_input == "A":
            access_command = input("Enter the access command for the object: ")
            description = input("Enter the description for the object: ")

            new_object = {
                "command": access_command,
                "description": description
            }
            games.append(new_object)

            with open("gamelist.json", "w") as json_file:
                json.dump(games, json_file, indent=4)
                print("\nObjects have been updated and saved to 'objects.json'.")
            print("\nUpdated objects in the file:")
            for game in games:
                print(f"{game['command']}: {game['description']}")

            gamemanager()

    elif user_input == "B":
            if not games:
                print("No objects to delete.")
            else:
                print("\nChoose an object to delete:")
                for index, game in enumerate(games, start=1):
                    print(f"{index}. ({game['command']}): {game['description']}")

                try:
                    delete_index = int(input("Enter the number of the object to delete: "))
                    if 1 <= delete_index <= len(games):
                        deleted_object = games.pop(delete_index - 1)
                        print(f"\nDeleted object: ({deleted_object['command']}): {deleted_object['description']}")

                        with open("gamelist.json", "w") as json_file:
                            json.dump(games, json_file, indent=4)
                            print("\nObjects have been updated and saved to 'objects.json'. Please restart.")
                    else:
                        print("\nInvalid selection. No object deleted.")
                except ValueError:
                    print("\nInvalid input. Please enter a valid number.")

    else:
        if user_input == "C":
                run = input("Enter a program to access. ")
                file_path = run

                if os.path.exists(file_path):
                    print(f"File existence confirmed. Executing")
                    import subprocess
                    subprocess.run(["python", run])

                else:
                    print(f"File not found. Press enter to return.")
                    gamemanager()

gamemanager()