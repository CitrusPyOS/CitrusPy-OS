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

def main():
    print("Calculator")
    print("__________")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("Enter a calculation: ")

        if user_input.lower() == "exit":
            print("Exiting...")
            break

        try:
            result = eval(user_input)
            print(f"Result:{result}")
        except Exception as e:
            print(f"Error: {e}. Please try again.")

if __name__ == "__main__":
    main()