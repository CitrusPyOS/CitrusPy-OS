import json

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