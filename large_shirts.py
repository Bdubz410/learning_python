# Modify the make_shirt function so that shirts are large by default with a message that reads I love Python.
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
def make_shirt(size='large', message="I love Python!"):
    """Your I love Python shirt"""
    print(f"\nYour shirt size is {size}.")
    print(f"The message printed on your shirt will be {message}.")

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'I am learning Python!')