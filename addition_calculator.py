# Wrap your code from addition.py exercise in a while loop so the user can continue entering numbers,
# even if they make a mistake and enter text instead of a number.
print("Give me two numbers and I will add them together.")
print("Enter 'q' to quit.")

while True:
    first_number = input('\nFirst number: ')
    if first_number == 'q':
        break
    second_number = input('\nSecond number: ')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print('Only enter numerical numbers!')
    else:
        print(answer)