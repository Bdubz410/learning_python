# Refactoring
# Often your code will eventually work, but you'll recognize that you could improve the code by
# breaking it up into a series of functions that have specific jobs. This process is called refactoring.
# Refactoring makes your code cleaner, easier to understand, and easier to extend.
# We can refactor remember_me.py by moving the bulk of its logic into one or more functions.
#from pathlib import Path
#import json

#def greet_user():
 #   """Greet the user by name."""
  #  path = Path('username.json')
   # if path.exists():
    #    contents = path.read_text()
     #   username = json.loads(contents)
      #  print(f"Welcome back, {username}!")
    #else:
     #   username = input("What is your name? ")
      #  contents = json.dumps(username)
       # path.write_text(contents)
        #print(f"We'll remember you when you come back, {username}!")


#greet_user()

# Let's refactor greet_user() so it's not doing so many different tasks. We'll start by moving
# the code for retrieving a stored username to a separate function.
#from pathlib import Path
#import json


#def get_stored_username(path):
 #   """Get stored username if available."""
  #  if path.exists():
   #     contents = path.read_text()
    #    username = json.loads(contents)
     #   return username
    #else:
     #   return None


#def greet_user():
 #   """Greet the user by name."""
  #  path = Path('username.json')
   # username = get_stored_username(path)
    #if username:
     #   print(f"Welcome back, {username}!")
    #else:
     #   username = input("What is your name? ")
      #  contents = json.dumps(username)
       # path.write_text(contents)
        #print(f"We'll remember you when you come back, {username}!")


#greet_user()

# We should factor one more block of code out of greet_user(). If the username doesn't exist, we should move the code
# that prompts for a new username to a function dedicated to that purpose.
from pathlib import Path
import json


def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")


greet_user()