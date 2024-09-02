# Working with Multiple Files
# Let's add more books to analyze, but before we do, let's move the bulk of this program to a function called
# count_words(). This will make it easier to run the analysis for multiple books.
from pathlib import Path


def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")
    path = Path('alice.txt')

# Now we can write a short loop to count the words in any text we want to analyze.
# First, we store the names of the files we want to analyze in a list then call count_words() for each file in the list.
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt',
             'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)

# Failing Silently
# To make a program fail silently, you write a try block as usual, but you explicitly tell Python to do nothing
# in the except block. Python has a pass statement that tells it to do nothing in a block.
from pathlib import Path


def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")
    path = Path('alice.txt')


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt',
             'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)