# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on
# the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the function a second time using keyword args.
def make_shirt(size, message):
    """Details of your shirt size and message"""
    print(f"\nYou chose size {size} for your shirt.")
    print(f"The shirt will say {message}")

make_shirt('small', "It's a crazy world we live in!")
make_shirt(size='medium', message="This shit is wild!")