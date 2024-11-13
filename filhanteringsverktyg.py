# import os  # Lägg till import av os-modulen

# # Filhanteringsverktyg

# def read_file(filename):
#     if os.path.exists(filename):
#         with open(filename, "r") as file:  # Korrigerat filnamn
#             content = file.readlines()
#             for line in content:
#                 print(line.strip())
#     else:
#         print("The file does not exist")

# def create_file(filename):
#     if not os.path.exists(filename):
#         with open(filename, "w") as file:
#             print(f"File was created: {filename}")

# def append_file(filename, text):
#     with open(filename, "a") as file:
#         file.write(text + "\n")
#     print("Text was added")

# # Main program

# while True:
#     print("Menu:")
#     print("1. Read a file")
#     print("2. Create a file")
#     print("3. Append to file")
#     print("4. Erase file")
#     print("5. Exit")

#     choice = input("Choose an option (1-5): ")

#     if choice == '1':
#         filename = input("Select file: ")
#         read_file(filename)
#     elif choice == '2':
#         filename = input("Enter filename: ")
#         create_file(filename)
#     elif choice == '3':
#         filename = input("Enter filename: ")
#         text = input("Text to add to file: ")
#         append_file(filename, text)  # Korrigerat till rätt funktion
