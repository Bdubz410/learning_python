# Exceptions
# Python uses special objects called exceptions to manage errors that arise during a program's execution.
# Whenever an error occurs that makes Python unsure of what to do next, it creates  an exception object.
# If you write code that handles the exception, the program will continue running.
# Exceptions are handled with try-except blocks, which asks Python to do something, but it also tells Python what to do
# if an exception is raised.
#
# When you use try-except blocks, your programs will continue running even if things start to go wrong.

# Handling the ZeroDivisionError Exception
#print(5/0)

# Using try-except Blocks
# When you think an error may occur you can write a try-except block to handle the exception.
# Here's what a try-except block for handling the ZeroDivisionError exception looks like.
try:
    print(5/0)
except ZeroDivisionError:
    print("You cannot divide by zero")

# Using Exceptions to Prevent Crashes
# This program does nothing to handle errors which is not a good thing.
#print("Give me two numbers, and I'll divide them.")
#print("Enter 'q' to quit.")

#while True:
    #first_number = input("\nFirst number: ")
    #if first_number == 'q':
        #break
    #second_number = input("\nSecond number: ")
    #if second_number == 'q':
        #break
    #answer = int(first_number) / int(second_number)
    #print(answer)
# It will give the user a traceback error which is confusing for nontechnical individuals. If a malicious user sees a
# traceback error, they will learn more than you want them to about your code.
# They'll know the name of your program file, and they will see a part of your code that isn't working properly.
# A skilled attacker can sometimes use this information to determine which kind of attacks to use against your code.

# The else Block
# We can make this program more error resistant by wrapping the line that might produce errors in a try-except block.
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst_number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
# The only code that should go in a try block is code that might cause an exception to be raised.
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You cannot divide by 0!")
# Any code that depends on the try block succeeding is added to the else block.
    else:
        print(answer)