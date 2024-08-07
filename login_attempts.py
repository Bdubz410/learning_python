# Add an attribute called login_attempts to your User class from exercise on page 162 (users).
# Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
# Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts() several times.
# Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts().
# Print login_attempts again to make sure it was reset to 0.
class User:
    """List attributes for a user profile."""

    def __init__(self, first_name, last_name, username, email, phone_number):
        """Describe a user profile."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.phone_number = phone_number
        self.login_attempts = 0

    def describe_user(self):
        """Print summary of user information."""
        print(f"\nName: {self.first_name} {self.last_name}"
              f"\nUsername: {self.username}"
              f"\nEmail Address: {self.email}"
              f"\nPhone Number: {self.phone_number}")

    def greet_user(self):
        """Personalize a greeting for the users."""
        print(f"\tHey {self.username} welcome to our amazing website!")

    def increment_login_attempts(self):
        """Increment the login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts to zero."""
        self.login_attempts = 0


user = User('Mr.', 'Python', 'PythonMaster101', 'anymail@email.com', '555-432-6987')

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login Attempts: {user.login_attempts}")

user.reset_login_attempts()
print(f"Login Attempts: {user.login_attempts}")