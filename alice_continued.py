# Let's build on the example from alice.py and see how exception handling can help when you're
# working with more than one file.

# Analyzing Text
# Let's pull in the text of Alice in Wonderland and try to count the number of words in the text.
# To do this we will use the string method split(), which by default splits a string wherever it finds any whitespace.
from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, that file doesn't exist.")
else:
    # Count the approximate number of words in the file:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")