# Working with a File's Contents
# We will first attempt to build a single string containing all the digits in the file with no whitespace in it.
# We start by reading the file and storing each line of digits in a list, as we did earlier.
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

#lines = contents.splitlines()
# We then create a variable, pi_string, to hold the digits of pi.
pi_string = ''
# We write a loop that adds each line of digits to pi_string.
for line in contents.splitlines():
    pi_string += line.lstrip() # use lstrip() to get rid of the whitespace to the left on each line.

# We print this string and also show how long the string is.
print(pi_string)
print(len(pi_string))

# Large Files: One Million Digits
from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()

#lines = contents.splitlines() ** to be more concise we can remove this line and change the code below.
pi_string = ''
# We change for line in lines: to for line in contents.splitlines():
#for line in lines:
for line in contents.splitlines():
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))