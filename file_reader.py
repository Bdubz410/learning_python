# Reading the Contents of a File
# Create a text document named pi_digits.txt.
# Here's a program that opens this file, reads it, and print the contents for the file to the screen:
from pathlib import Path

# Here we build a Path object representing the file pi_digits.txt, which we assign to the variable path.
# Since this file is saved in the same directory as the .py file we're writing,
# the file name is all that Path needs to access the file.
path = Path('pi_digits.txt')
# Once we have a Path object representing pi_digits.txt, we use the read_text()
# method to read the entire contents of the file.
contents = path.read_text()
# The contents of the file are returned as a single string, which we assign to the variable contents.
# When we print the value of contents, we see the entire contents of the text file.
print(contents)
# The only difference between this output and the original file is the extra blank line at the end of the output.
# The blank line appears because read_text() returns an empty string when it reaches the end of the file;
# this empty string shows up as a blank line.

# We can remove the extra blank line by using rstrip() on the contents string.
# rstrip() method removes, or strips, any whitespace characters from the right side of the string.
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
contents = contents.rstrip()
print(contents)

# We can strip the trailing newline characters when we read the contents of the file, by applying the rstrip()
# immediately after read_text()
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text().rstrip()
# The cleaned-up string is then assigned to the variable contents. This approach is called method chaining.
print(contents)

# Relative and Absolute File Paths
# A relative file path tells Python to look for a given location relative to the directory where the
# currently running program file is stored.
# To get Python to open files from a directory other than the one where your program file is stored, you need
# provide the correct path.
# For example: we need to build a path that starts with the directory text_files, and ends with the filename:
path = Path('text_files/filename.txt')

# An absolute path is exactly where the file is on your computer.
# Absolute paths are usually longer than relative paths, because they start at you system's root folder:
path = Path('/home/eric/data_files/text_files/filename.txt')

# **Windows uses '\' in file paths**  **Python uses '/' for ALL path names**
# ****ALWAYS USE '/' IN YOUR CODE****