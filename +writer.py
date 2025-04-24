import tkinter as tk

def create_file():
    global file_name  
    file_name = input("Enter the name of the file to create (with extension, e.g., 'example.txt'): ")
    try:
        with open(file_name, 'w') as f:
            print(f"File '{file_name}' has been created successfully!")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

def open_file_via_terminal():
    global file_name  
    file_name = input("Enter the name of the file to open (with extension, e.g., 'example.txt'): ")
    try:
        with open(file_name, 'r') as f:
            content = f.read()
            text_area.delete(1.0, tk.END)  
            text_area.insert(tk.END, content)  
        print(f"File '{file_name}' has been opened successfully!")
    except FileNotFoundError:
        print(f"File '{file_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred while opening the file: {e}")

def save_to_created_file():
    try:
        if file_name:  
            with open(file_name, 'w') as f:
                f.write(text_area.get(1.0, tk.END))
                print(f"Content has been saved to '{file_name}' successfully!")
        else:
            print("No file has been created or opened yet. Use 'Create File (Terminal)' or 'Open File (Terminal)' first.")
    except NameError:
        print("No file has been created or opened yet. Use 'Create File (Terminal)' or 'Open File (Terminal)' first.")
    except Exception as e:
        print(f"An error occurred while saving to the file: {e}")

def clear_text():
    text_area.delete(1.0, tk.END)

root = tk.Tk()
root.title("+Writer")

text_area = tk.Text(root, wrap='word', font=("Arial", 12))
text_area.pack(expand=True, fill='both')

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Create File (Terminal)", command=create_file)
file_menu.add_command(label="Open File (Terminal)", command=open_file_via_terminal)
file_menu.add_command(label="Save to Created File", command=save_to_created_file)
file_menu.add_command(label="Clear", command=clear_text)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

root.mainloop()
