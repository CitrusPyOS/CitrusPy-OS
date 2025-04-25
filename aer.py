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
import subprocess
import sys

logged_in = False

def aer(filename):
    while True:
        user_input = input("(A) Append | (E) Edit Line | (R) Remove Line | (Q) Quit: ").strip().upper()

        if user_input == "A":
            with open(filename, "a") as file:
                text = input("Enter something: ")
                file.write(text + "\n")
            print("\n--- Updated File Content ---")
            with open(filename, "r") as file:
                print(file.read())

        elif user_input == "E":
            try:
                with open(filename, "r") as file:
                    lines = file.readlines()
                print("\n--- File Content ---")
                for i, line in enumerate(lines, start=1):
                    print(f"{i}: {line.strip()}")
                line_number = int(input("Enter the line number to edit: "))
                if 1 <= line_number <= len(lines):
                    new_text = input("Enter new text for the line: ")
                    lines[line_number - 1] = new_text + "\n"
                    with open(filename, "w") as file:
                        file.writelines(lines)
                    print("\n--- Updated File Content ---")
                    with open(filename, "r") as file:
                        print(file.read())
                else:
                    print("Invalid line number.")
            except FileNotFoundError:
                print(f"Error: The file '{filename}' does not exist.")

        elif user_input == "R":
            try:
                with open(filename, "r") as file:
                    lines = file.readlines()
                print("\n--- File Content ---")
                for i, line in enumerate(lines, start=1):
                    print(f"{i}: {line.strip()}")
                line_number = int(input("Enter the line number to remove: "))
                if 1 <= line_number <= len(lines):
                    del lines[line_number - 1]
                    with open(filename, "w") as file:
                        file.writelines(lines)
                    print("\n--- Updated File Content ---")
                    with open(filename, "r") as file:
                        print(file.read())
                else:
                    print("Invalid line number.")
            except FileNotFoundError:
                print(f"Error: The file '{filename}' does not exist.")

        elif user_input == "Q":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

def main():
    while True:
        print("\nAER Text Editor v.0.1")
        print("_______________________")
        print("1. Create a new file or open an existing file")
        print("Q. Quit")

        user_input = input("Choose an option: ").strip().upper()
        if user_input == "1":
            filename = input("Enter filename (+ extension): ").strip()
            try:
                with open(filename, "a") as file:
                    text = input("Enter something: ")
                    file.write(text + "\n")
            except FileNotFoundError:
                print(f"Error: Could not create file '{filename}'.")
            else:
                print("\n--- File Content ---")
                with open(filename, "r") as file:
                    print(file.read())
                aer(filename)

        elif user_input == "Q":
            print("ExItInG")
            subprocess.Popen(['python', 'user_input.py'])
            sys.exit()

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
