# Positional arguments
# When you call a function, Python must match each argument in the function call with a
# parameter in the function definition. The way to do this is based on the order of the arguments provided.
# Values matched up this way are called positional arguments.
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# In positional arguments order matters. You can get unexpected results when you mix up the arguments.
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Keyword arguments is a name-value pair that you pass to a function.
# Keyword arguments free you from having to worry about correctly ordering your arguments in the function call.
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# The order of keyword arguments does not matter because Python knows where each value should go.
describe_pet(animal_type='hamster', pet_name='harry')
# We will rewrite the function call out with a new order
describe_pet(pet_name='harry', animal_type='hamster')

# Default Values; can be defined for each parameter
# The order has changed because pet_name here is still a positional argument.
# When using a default value it should be listed after all the parameters that don't have default values.
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
# We can call the function again, this time using only a pets name as the argument.
# Since Python interprets this as a positional argument, the argument will match up with the first parameter
# listed in the function's definition.
describe_pet('willie')
# To describe an animal other than a dog , use a function call like this
describe_pet(pet_name='harry', animal_type='hamster')

# Equivalent function calls
# Positional arguments, keyword arguments, and default values can all be used together, we will often have several
# equivalent ways to call a function.
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# All of the following calls will work for this function
# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry
describe_pet('harry', 'hamster')
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# Avoiding argument errors; unmatched arguments occur when you provide fewer or more arguments than a function needs.
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")

describe_pet()