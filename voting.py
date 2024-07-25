# Simple if Statements
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Are you registered to vote?")

# Testing the output for someone under the age limit
age = 17
if age >= 18:
    print("You are old enough to vote!")   # Test did not pass so no output printed

# if-else Statements
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Are you registered to vote?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")