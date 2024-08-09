# An administrator is a special kind of user. Write a class called Admin that inherits
# from the User class from page 162 or page 167. Add an attribute, privileges, that stores a list of strings like
# "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator's set of privileges.
# Create an instance of Admin, and call your method.
class User:
    """List attributes for a user profile."""

    def __init__(self, first_name, last_name, username, email, phone_number):
        """Describe a user profile."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.phone_number = phone_number

    def describe_user(self):
        """Print summary of user information."""
        print(f"\nName: {self.first_name} {self.last_name}"
              f"\nUsername: {self.username}"
              f"\nEmail Address: {self.email}"
              f"\nPhone Number: {self.phone_number}")

    def greet_user(self):
        """Personalize a greeting for the users."""
        print(f"\tHey {self.username} welcome to our amazing website!")


class Admin(User):
    """List attributes for an admin profile."""

    def __init__(self, first_name, last_name, username, email, phone_number):
        """Describe a user profile.
        Describe an admin profile.
        """
        super().__init__(first_name, last_name, username, email, phone_number)
        self.privileges = ["can add post", "can delete post", "can ban user", "can sensor content"]

    def show_privileges(self):
        """List the admins privileges."""
        print(f"Admin functions: {self.privileges}")


admin = Admin('super', 'user', 'AdminAdmin', 'admin@email.com', 555-345-6897)
admin.show_privileges()