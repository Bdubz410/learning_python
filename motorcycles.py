# Modifying, adding, and removing elements

# Modifying elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Appending elements to the end of a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

# Adding items to an empty list
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

# Inserting elements into a list
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)

# Removing items from a list
# Using the del statement to remove item
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles.insert(0, 'honda')  # Add honda back to show how to use del in the next lines to delete a different index.
print(motorcycles)

del motorcycles[1]
print(motorcycles)  # del deletes the item

# Removing an item using the pop() method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# The pop() method removes the last item from a list, but it lets you work with that item after removing it.
popped_motorcycles = motorcycles.pop()  # Pop a value from the list and assign it to a new variable
print(motorcycles)
print(popped_motorcycles)  # Print the popped value to prove that we still have access to the value that was removed.

# Print a statement about the last motorcycle you bought.
motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print(f'The last motorcycle I bought was {last_owned.title()}.')

# Popping items from any position in a list.
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print(f'The first motorcycle I owned was a {first_owned.title()}.')  # pop removes the item but it can still be accessed.

# Removing an item by value with the remove() method
# Sometimes we may not know the position of the value we want to remove so we use the remove() method to find the value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# Using remove() method to remove an item but this time adding a reason
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")


