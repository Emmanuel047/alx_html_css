import json

# Prompt the user to enter the filename of the JSON file.
filename = input("Enter the filename of the JSON file: ")

# Open the file and read its contents.
with open(filename, "r") as f:
    data = json.load(f)

# Print the contents of the JSON file.
print(data)