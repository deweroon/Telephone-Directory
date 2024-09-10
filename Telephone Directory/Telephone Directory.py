# Create an empty phone directory
phone_directory = {}

def add_number(name, number):
    phone_directory[name] = number
    print(f"Number added for {name}.")

def search_number(name):
    number = phone_directory.get(name)
    if number:
        print(f"Number for {name}: {number}")
    else:
        print(f"{name} not found.")

def list_directory():
    if phone_directory:
        print("Phone Directory:")
        for name, number in phone_directory.items():
            print(f"{name}: {number}")
    else:
        print("No entries in the directory.")

# User interface
while True:
    print("\n1. Add Number")
    print("2. Search Number")
    print("3. List Directory")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        add_number(name, number)
    elif choice == '2':
        name = input("Enter the name you want to search: ")
        search_number(name)
    elif choice == '3':
        list_directory()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid option, please try again.")