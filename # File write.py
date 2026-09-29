with open("notes.txt", "a") as file:
    notes1 = input("Enter first line of notes: ")
    file.write(notes1 + "\n")
    notes2 = input("Enter second line of notes: ")
    file.write(notes2 + "\n")
with open("notes.txt", "r") as file:
    content = file.read()
    print("\n--- Updated File Content ---")
    print(content)