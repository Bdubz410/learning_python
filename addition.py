# One common problem when prompting for numerical input occurs when people provide text instead of numbers.
# When you try to convert the input to an int, you'll get a ValueError.
# Write a program that prompts for two numbers. Add them together and print the result.
# Catch the ValueError if either input value is not a number, and print a friendly error message.
# Test your program by entering two numbers and then by entering some text instead of a number.
print("Give me two numbers and I will add them for you.")

first_number = input('\nFirst number: ')
second_number = input('\nSecond number: ')
try:
    answer = int(first_number) + int(second_number)
except ValueError:
    print("You can only use numerical numbers.")
else:
    print(answer)