import random
import string

class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def generate_password(self, length=12):
        chars = string.ascii_letters + string.digits + "!@#$%^&*()"
        return "".join(random.choice(chars) for _ in range(length))

    def add_password(self, site, username, password):
        if site in self.passwords:
            print(f"Password already exists. Saved new password.")
        self.passwords[site] = {"username": username, "password": password}
        print(f"Password saved.")

    def get_password(self, site):
        if site in self.passwords:
            info = self.passwords[site]
            print(f"Site: {site}\nUsername: {info['username']}\nPassword: {info['password']}")
        else:
            print("No password found.")
    def list_sites(self):
        if self.passwords:
            print("Saved sites:")
            for site in self.passwords:
                print(f"- {site}")
        else:
            print("No sites saved yet.")