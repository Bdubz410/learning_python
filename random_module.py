# The Python Standard Library
# This library is a set of modules included with every Python installation.
# Now you can start using modules like these that other programmers have written.
# You can use any function or class in the standard library by including a simple import statement at the top of the
# file. Let's take a look at one module, random, which can be useful in modeling many real-world situations.

# **RUN IN TERMINAL**
# One interesting function from the random module is randint(). This function takes two integer arguments and returns
# a randomly selected integer between (and including) those numbers.
from random import randint
randint(1, 6)

# Another useful function is choice(). This function takes in a list or tuple and returns a randomly chosen element:
from random import choice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
first_up

# ***The random module shouldn't be used when building security-related applications, just for fun.***