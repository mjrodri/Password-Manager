import json
import getpass

def load_passwords():
    try:
        with open('passwords.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_passwords(passwords):
    with open('passwords.json', 'w') as file:
        json.dump(passwords, file, indent=4)

def add_password():
    service = input("Enter the name of the service: ")
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    passwords = load_passwords()
    passwords[service] = {'username': username, 'password': password}
    save_passwords(passwords)
    print("Password added successfully!")

def get_password():
    service = input("Enter the name of the service: ")
    passwords = load_passwords()
    if service in passwords:
        print("Username:", passwords[service]['username'])
        print("Password:", passwords[service]['password'])
    else:
        print("Service not found in the password archive.")

def main():
    print("Welcome to the Password Archive!")
    while True:
        print("\nMenu:")
        print("1. Add a new password")
        print("2. Retrieve a password")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_password()
        elif choice == '2':
            get_password()
        elif choice == '3':
            print("Thank you for using Password Archive. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
