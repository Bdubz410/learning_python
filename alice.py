# Handling the FileNotFoundError Exception
# One common issue when working with files is handling missing files.
# The file might be in a different location, the filename might be misspelled, or just nonexistent.
# This can be handled with a try-except block.
# The following program tries to read in the contents of Alice in Wonderland, but we haven't saved to file alice.txt
# in the same directory as alice.py
#from pathlib import Path

#path = Path('alice.txt')
# The encoding argument is needed when your system's default encoding doesn't match
# the encoding of the file that's being read.
#contents = path.read_text(encoding='utf-8')

# To handle this error that's being raised, the try-block will begin with the line that was identified as problematic
# in the traceback. In our example, this is the line that contains read_text(). Here's how to fix this:
from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")