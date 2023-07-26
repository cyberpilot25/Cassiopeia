import json
import random

# Define the password manager class.
class PasswordManager:

    def __init__(self):
        # Create a dictionary to store the passwords.
        self.passwords = {}

    # Add a password to the password manager.
    def add_password(self, website, username, password):
        # Check if the website already exists in the dictionary.
        if website in self.passwords:
            # The website already exists, so raise an exception.
            raise ValueError("Website already exists.")

        # The website does not exist, so add it to the dictionary.
        self.passwords[website] = {
            "username": username,
            "password": password,
        }

    # Get a password for a given website.
    def get_password(self, website):
        # Check if the website exists in the dictionary.
        if website not in self.passwords:
            # The website does not exist, so raise an exception.
            raise ValueError("Website does not exist.")

        # The website exists, so return the password.
        return self.passwords[website]["password"]
