import os
from tkinter import Tk, filedialog

languages = []

while True:
    name = input('Please type a name of com lang you know (or type "exit" to finish): ')
    if name.lower() == "exit":
        break
    if name.strip():
        languages.append(name.strip())

print("Then save these names on a text file ....")

root = Tk()
root.withdraw()

filename = filedialog.asksaveasfilename(
    title="no1_test",
    defaultextension=".txt",
    filetypes=[("Text files", "*.txt")]
)

if filename:
    if os.path.exists(filename):
        print("That file already exists. Please choose a new filename.")
    else:
        with open(filename, "x") as file:
            for language in languages:
                file.write(language + "\n")
        print("Names saved successfully.")
else:
    print("Saving cancelled.")

root.destroy()
