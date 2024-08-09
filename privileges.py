# Write a separate Privileges class. The class should have one attribute, privileges,
# that stores a list of strings as described in Admin (exercise 9-7).
# Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class.
# Create a new instance of Admin and use your method to show its privileges.
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


class Privileges:
    """List privileges for admin profile."""

    def __init__(self):
        """Initialize the admin's privileges."""
        self.privileges = ["can add post", "can delete post", "can ban user", "can sensor content"]

    def show_privileges(self):
        """List the admins privileges."""
        print(f"Admin functions: {self.privileges}")


class Admin(User):
    """List attributes for an admin profile."""

    def __init__(self, first_name, last_name, username, email, phone_number):
        """Describe a user profile.
        Describe an admin profile.
        """
        super().__init__(first_name, last_name, username, email, phone_number)
        self.privileges = Privileges()


admin = Admin('super', 'user', 'AdminAdmin', 'admin@email.com', 555-345-6897)
admin.privileges.show_privileges()