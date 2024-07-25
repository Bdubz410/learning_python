# Making a list with just even numbers using range() function.

even_numbers = list(range(2, 11, 2))
print(even_numbers)

# We can do statistics with a list of numbers in the TERMINAL
# create the list of digits for example;
# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# sum(digits)    to get the sum from the list
# min(digits)    to get the minimum digit from the list
# max(digits)    to get the maximum digit number from the list.

even_numbers = list(range(2, 21, 2))
for even in even_numbers:
    print(even)