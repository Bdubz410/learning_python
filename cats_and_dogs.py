# Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first file and three dogs in second
# file. Write a program that tries to read these files and print the contents of the file to the screen.
# Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is
# missing. Move one of the files to a different location on your system, and make sure the code in the except block
# executes properly.
from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print(f"\nReading file: {filename}")

    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print("Sorry I cannot find that file.")
    else:
        print(contents)