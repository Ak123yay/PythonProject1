import random
import string

class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def generate_password(self, length=8):
        chars = string.ascii_letters + string.digits + "!@#$%^&*()"
        return "".join(random.choice(chars) for _ in range(length))

    def add_password(self, site, username, password):
        self.passwords[site] = {"username": username, "password": password}

    def get_password(self, site):
        return self.passwords.get(site)

    def list_sites(self):
        return list(self.passwords.keys())

def main():
    manager = PasswordManager()
    while True:
        print("\nPassword Manager")
        print("1. Generate a password")
        print("2. Retrieve a password")
        print("3. Saved sites")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            site = input("Site name: ")
            username = input("Username: ")
            length = input("Password length: ")
            length = int(length) 
            password = manager.generate_password(length)
            manager.add_password(site, username, password)
            print(f"Generated password: {password}")
        elif choice == "2":
            site = input("Site name: ")
            info = manager.get_password(site)
            if info:
                print(f"Username: {info['username']}, Password: {info['password']}")
            else:
                print("No site found.")
        elif choice == "3":
            sites = manager.list_sites()
            print("Saved sites:", ", ".join(sites) if sites else "None")
        elif choice == "4":
            break
        else:
            print("Try again.")

if __name__ == "__main__":
    main()