# Saving and Reading User Generated Data
# Saving data with json is useful when you're working with user-generated data, because if you don't store your user's
# information somehow, you'll lose it when the program stops running.
from pathlib import Path
import json


path = Path('username.json')
# The exists() method returns True if a file or folder exists and False if it does not exist.
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}!")
else:
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")