# Organizing a list
# Sorting a list permanently with the sort() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)  # sort() will permanently sort the list alphabetically; we can never revert to the original order

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)  # Sorts the list in reverse-alphabetical order permanently
print(cars)

# Sorting a list temporarily with the sorted() function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))  # Will temporarily sort in alphabetical order

print("\nHere is the original list again:")
print(cars)

print("\nHere is the list in reverse order:")
cars.sort(reverse=True)
print(cars)

# Printing a list in reverse order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()  # This will reverse the list permanently; you can revert back by applying reverse() to the same list a second time.
print(cars)

cars.reverse()
print(cars)

# Finding the length of a list by using the len() function
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)  # Run this in **TERMINAL**