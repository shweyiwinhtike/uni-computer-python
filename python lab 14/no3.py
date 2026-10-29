filename = input("Enter a filename: ")
old_string = input("Enter the string to be replaced: ")
new_string = input("Enter the new string to replace the old string: ")

try:
    with open(filename, "r") as file:
        content = file.read()

    if old_string not in content:
        print("The old string was not found in the file.")
    else:
        content = content.replace(old_string, new_string)

        with open(filename, "w") as file:
            file.write(content)

        print("The file is now updated, and its new content is:")
        print(content, end="" if content.endswith("\n") or content == "" else "\n")

except FileNotFoundError:
    print("File not found.")
