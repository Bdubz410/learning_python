# Start with a copy of your program from messages.py.
# Write a function called send_messages() that prints each text message and moves each message to a new list
# called sent_messages as it's printed. After calling the function,
# print both of your lists to make sure the messages were moved correctly.
messages = ['Hey there', 'Hi there', 'Hello there']
sent_messages = []

def show_messages(messages, sent_messages):
    """Print a series of text messages"""
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)

def send_messages(sent_messages):
    """Print all the messages."""
    for sent_message in sent_messages:
        print(sent_message)

show_messages(messages, sent_messages)
send_messages(sent_messages)
# Testing if the list printed empty; in archived_messages.py it wants me to prevent list from modifying
print(messages)