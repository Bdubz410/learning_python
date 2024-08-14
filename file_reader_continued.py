# Accessing a File's Lines
# You can use the splitlines() method to turn a long string into a set of lines, and then use a for loop to examine
# each line from a file, one at a time.
from pathlib import Path

path = Path('pi_digits.txt')
# We start out by reading the entire contents of the file.
contents = path.read_text()

# The splitlines() method returns a list of all lines in a file, and we assign this list to the variable lines.

# We then loop over these lines and print each one.
for line in contents.splitlines():
    print(contents)
