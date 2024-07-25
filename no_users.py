# Add an if test to hello_admin.py to make sure the list of users is not empty.
# If the list is empty, print the message We need to find some users!
# Remove all the usernames from your list, and make sure the correct message is printed.

usernames = []

if usernames:
    for user in usernames:
        print(f"Hey there {user}, welcome to the best page ever!")
else:
    print("We need to find some users!")