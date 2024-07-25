# How the input() function works
#message = input("Tell me something , and I will repeat it back to you: ")
#print(message)

# parrot.py continued
# Letting the user choose when to quit.
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
# Right now if user inputs 'quit' Python will print quit; to fix this we will add an if test.
    print(message)

# Entering an if test
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)