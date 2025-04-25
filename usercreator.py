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