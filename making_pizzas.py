# We made this file in the same directory as pizza_2.py. This file imports the module pizza_2.py.
# then makes two calls to make_pizza()
import pizza_2

pizza_2.make_pizza(16, 'pepperoni')
pizza_2.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# Importing Specific Functions
# You can also import a specific function from a module. With this syntax:
# from module_name import function_name

# You can import as many functions as you want from a module using a comma for separation:
# from module_name import function_0, function_1, function_2

# The making_pizzas.py example would look like this if we want to import just the function we're going to use:
# from pizza_2 import make_pizza

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# NOTE: with the above syntax you don't need the (.) notation when you call a function.
# Because we've explicitly imported the function make_pizza() in the import statement, we can call it by name when we
# use the function.

# Using as to Give a Function an Alias
# This will be done if the name of the function will conflict with the current program being written or if the name is
# just too long.
from pizza_2 import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using as to Give a Module an Alias
# This alias shortens the module name and is more concise when calling p.make_pizza() than calling pizza.make_pizza()
import pizza_2 as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Importing All Functions in a Module
# You can tell Python to import every function in a module by using the (*) operator.
from pizza_2 import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# The asterisk tells Python to copy every function from the module pizza_2 into this program.
# Because every function is imported, you can call each function by name without using the dot notation.
# As a best practice do not use this method due to potential possible function names matching in larger code, this is
# shown here to recognize when we see it in code.
# The best approach is to import the function or functions you want, or import the entire module and use the . notation