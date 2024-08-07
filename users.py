# Make a class called User. Create two attributes called first_name and last_name,
# and then create several other attributes that are typically stored in a user profile.
# Make a method called describe_user() that prints a summary of the user's information.
# Make another method called greet_user() that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.
class User:
    """List attributes for a user profile."""
    def __init__(self, first_name, last_name, username, email, phone_number):
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


user_one = User('Johnny', 'Mittens', 'Meow1234', 'kittymittens@email.com', '555-345-6897')
user_two = User('Captain', 'America', 'Marvel4lyfe', 'avengers@email.com', '555-984-7896')
user_three = User('Leonitus', 'Doggins III', '3rdisBetterThan1', 'woof@email.com', '534-888-3695')
user_four = User('Luna', 'Moon', 'LuvU2daMoon', 'Nasa@email.com', '555-802-4538')

user_one.describe_user()
user_one.greet_user()

user_two.describe_user()
user_two.greet_user()

user_three.describe_user()
user_three.greet_user()

user_four.describe_user()
user_four.greet_user()