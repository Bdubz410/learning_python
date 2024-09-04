# Storing Data
# JSON (JavaScript Object Notation) format was originally created for JavaScript. It has since become a common format
# used by many languages including Python.
# We store data that users provide in a data structure like a list or dictionary.
# When users close a program, we will want them to be able to save the data. A simple way to do this involves storing
# the data using the json module.
# The json module allows you to convert simple Python data structures into JSON formatted strings,
# and then load the data from that file the next time the program runs.

# Using json.dumps() and json.loads()
from pathlib import Path
# first import json module
import json

numbers = [2, 3, 5, 7, 11, 13]

# choose filename; it's customary to use .json to indicate the data is stored in the JSON format.
path = Path('numbers.json')
# use json.dumps() function to generate a string containing the JSON representation of the data.
contents = json.dumps(numbers)
# once we have this string, we write it to the file using the write_text() method used earlier.
path.write_text(contents)