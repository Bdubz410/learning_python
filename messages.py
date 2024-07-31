# Make a list containing a series of short text messages.
# Pass the list to a function called show_messages(), which prints each text message.
messages = ['Hey there', 'Hi there', 'Hello there']

def show_messages(messages_list):
    """Print a series of text messages"""
    for message in messages_list:
        print(message)

show_messages(messages)