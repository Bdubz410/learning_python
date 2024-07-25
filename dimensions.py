# Defining a tuple(); use a tuple when you want to store a set of values that
# should not be changed throughout the life of the program.
# Tuples are technically defined by a comma (,) we use parenthesis to look neater.
# If you want to define a tuple with one element, you need to include a trailing comma (,)
# It doesn't make sense to build a tuple with one element, but this can happen when tuples are generated automatically.

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#dimensions[0] = 250  This is a practice line; Python returns an error due to Tuples not being allowed modifications.

# Looping through all values in a tuple
for dimension in dimensions:
    print(dimension)

# Writing over a tuple
# Although you can't modify a tuple, you can assign a new value to a variable that represents a tuple.

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)    # Python doesn't raise an error because reassigning a variable is valid.
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)