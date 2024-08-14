# Is Your Birthday Contained in Pi?
# Let's find out if your birthday appears anywhere in the first million digits of pi.
# We can do this by expressing each birthday as a string of digits and seeing if that
# string appears anywhere in pi_string.
from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()

#lines = contents.splitlines()
pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")