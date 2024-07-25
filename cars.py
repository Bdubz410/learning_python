# A simple example of an if statement

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == ('bmw'):    # All cars should print in title case with the exception of bmw which should be all uppercase.
        print(car.upper())
    else:
        print(car.title())

#Conditional Tests

# Checking for equality in the TERMINAL
# At the heart of every if statement is an expression that can be evaluated as True or False
# this is called a conditional test. Python uses the values True and False to decide whether the code
# in an if statement should be executed. if a conditional test evaluates to True,
# Python executes the code following the if statement.
# If the test evaluates to False, Python ignores the code following the if statement.

# car = 'bmw'   # a single equal sign is a statement; this line can read "Set the value of car equal to bmw"
# car == 'bmw'   # a double equal sign asks a question "Is the value of car equal to bmw?"
# True

# Ignoring case when checking for equality. Testing for equality is case-sensitive in Python.

# car = 'Audi'
# car == 'audi'
# False

# If case matters, this behavior is advantageous.
# If case doesn't matter; you can convert the variable's value to a case type before comparing.

# car = 'Audi'
# car.lower() == 'audi'
# True