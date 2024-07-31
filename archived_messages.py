# Start with your work from sending_messages.py. Call the function send_messages() with a copy of the list of messages.
# After calling the function, print both of your lists to show that the original list has retained its messages.
messages = ['Hey there', 'Hi there', 'Hello there']
sent_messages = []

def show_messages(messages, sent_messages):
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)

def send_messages(sent_messages):
    for sent_message in sent_messages:
        print(sent_message)

show_messages(messages[:], sent_messages)
send_messages(sent_messages)
# Preventing the function from modifying the list with [:] after list we do not want to modify.
print(messages)