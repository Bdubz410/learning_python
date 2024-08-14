# You can use a loop to see how hard it might be to win the kind of lottery you just modeled.
# Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins.
# Print a message reporting how many times the loop had to run to give you a winning ticket.
import random

# Create a list containing 10 numbers and 5 letters
list_series = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Define your ticket.
my_ticket = [11, 'B', 27, 'D']

# Initialize the counter
attempts = 0

# Loop until the winning ticket matches your ticket.
while True:
    # Randomly select 4 items from the list
    winning_ticket = random.sample(list_series, 4)
    attempts += 1

    # Check if the winning ticket matches your ticket
    if set(winning_ticket) == set(my_ticket):
        break

# Print the number of attempts it took to get the winning ticket.
print(f"It took {attempts} attempts to get the winning ticket!")