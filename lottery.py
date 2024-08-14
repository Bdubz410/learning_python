# Make a list or tuple containing a series of 10 numbers and 5 letters. Randomly select 4 numbers or letters from
# the list and print a message saying that any ticket matching these 4 numbers or letters wins a prize.
import random

list_series = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

lottery_winner = random.sample(list_series, 4)

print(f"The winning lottery numbers/letters are: {lottery_winner} ")
print(f"Any ticket matching these numbers or letters wins a prize!")