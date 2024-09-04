# Modify your except block in cats_and_dogs.py to fail silently if either file is missing.
from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:

    path = Path(filename)
    print(f"\nReading file: {filename}")
    try:
        contents = path.read_text()
    except:
        pass
    else:
        print(contents)