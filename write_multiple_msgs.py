# Writing Multiple lines
# The write_text() method does a few thing behind the scenes. If the file that path points to doesn't exist.
# it creates that file. Also, after writing the string to the file, it makes sure the file is closed properly.
# To write more than one line to a file, you need to build a string containing the entire contents of the file,
# and then call write_text() with that string.
from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path('programming.txt')
path.write_text(contents)