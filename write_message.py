# Writing to a File
# Writing a Single Line
# Once you have a path defined you can write to a file using the write_text() method.
from pathlib import Path

path = Path('programming.txt')
path.write_text("I love Programming.")

# Python can only write strings to a text file. If you want to store numerical data in a text file, you'll have to
# convert the data to string format first using the str() function.
