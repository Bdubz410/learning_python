# Do the following to create a program that simulates how websites ensure that everyone has a unique username.
# Make a list of five or more usernames called current_users.
# Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
# Loop through the new_users list to see if each new username has already been used.
# If it has, print a message that the person will need to enter a new username.
# If a username has not been used, print a message saying that the username is available.
# Make sure your comparison is case-insensitive. If 'John' has been used, 'JOHN' should not be accepted.
# (To do this, you'll need to make a copy of current_users containing the lowercase versions of all existing users.)

current_users = ['John Smith', 'Jane Doe', 'Black Dahlia', 'Julius Caesar', 'Syd Vicious']
current_users_lower = [user.lower() for user in current_users]

new_users = ['Spicy Meatball', 'jane doe', 'Spicy_like_pepper', 'syd vicious', 'Nefarious Ninja']

for username in new_users:
    if username.lower() in current_users_lower:
        print(f"Sorry, {username} is taken, please choose another.")
    else:
        print(f"{username} is an available username!")

# Example current usernames
#current_users = ["John", "Admin", "Jack", "Ana", "Natalie"]

# Example new usernames
#new_users = ["Pablo", "Donald", "Calvin", "Natalie", "Emma"]

# Convert current usernames to lowercase for case-insensitive comparison
#current_users_lower = [user.lower() for user in current_users]

# Check new usernames
#for username in new_users:
#    if username.lower() in current_users_lower:
#        print(f"Username '{username}' is already taken. Please choose a different one.")
#    else:
#        print(f"Username '{username}' is available.")