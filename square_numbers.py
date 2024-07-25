# Making a list with square numbers using range() function

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# Can also write the program this way with the same outcome and less lines of code.

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# List comprehensions are more advanced way of writing code. This is a list comprehension to get the same outcome as the previous programs.

squares = [value**2 for value in range(1, 11)]
print(squares)
