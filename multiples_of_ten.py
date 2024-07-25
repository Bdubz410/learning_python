# Ask the user for a number, and then report whether the number is a multiple of 10 or not.
number = input("Give me a random number and I will tell you if it is a multiple of 10: ")
number = int(number)

if number % 10 == 0:
    print(f"\n{number} is a multiple of ten.")
else:
    print(f"\n{number} is not a multiple of ten.")