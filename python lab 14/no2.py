from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

filename = filedialog.askopenfilename(
    title="Open your previous file",
    filetypes=[("Text files", "*.txt")]
)

if not filename:
    print("No file selected.")
else:
    with open(filename, "r") as file:
        content = file.read()

    print("Your current file content is:")
    print(content, end="" if content.endswith("\n") or content == "" else "\n")

    new_languages = []

    while True:
        name = input('Please type a new name of com lang to add to your file (or type "exit" to finish): ')
        if name.lower() == "exit":
            break
        if name.strip():
            new_languages.append(name.strip())

    with open(filename, "a") as file:
        for language in new_languages:
            file.write(language + "\n")

    print("Then save these new names on your text file ....")
    print("Updated file content is:")
    with open(filename, "r") as file:
        print(file.read(), end="")

root.destroy()
