# Write a program that polls users about their dream vacation.
# Write a prompt similar to if you could visit one place in the world, where would you go?
# Include a block of code that prints the results of the poll.
responses = {}

polling_active = True

while polling_active:
    dream_vacation = input("If you could visit one place i the world, where would you go? ")

    responses[dream_vacation] = dream_vacation

    value = input("\nWould you like to let another person respond (yes/ no) ")
    if value == 'no':
        polling_active = False

print("\nThe Results: ")
for dream_vacation, value in responses.items():
    print(f"So your dream vacation would be to visit {dream_vacation}!")