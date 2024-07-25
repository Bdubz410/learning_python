# Working with part of a list
# slicing a list

players = ['charles', 'martina', 'michael', 'florence', 'eli']   # Print the first three players from the list
print(players[0:3])

players = ['charles', 'martina', 'michael', 'florence', 'eli']   # Print the second to fourth players from the list
print(players[1:4])

# Print the second to last players omitting the end of the index
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:])

# Print the beginning to the end without identifying an index
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:])

players = ['charles', 'martina', 'michael', 'florence', 'eli']  # Output the last three players using a negative integer
print(players[-3:])

# Looping through a slice; Can use a slice in a for loop if you want to loop through a subset of the elements in a list.

players = ['charles', 'martina', 'michael', 'florence', 'eli']
players[0] = 'bob'  # If I want to replace the first player with a new player
print(players)

for player in players[:3]:    # Looping through the first three players to print a roster
    print(player.title())

players = ['charles', 'martina', 'michael', 'florence', 'eli']  # Loop through last three players to print a roster
for player in players[-3:]:
    print(player.title())

players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[1:5]:
    print(player.title())

players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[-4:]:
    print(player.title())