# Think of at least five places in the world you'd like to visit.
# Store the locations in a list. Make sure the list is not in alphabetical order.
# Print your list in its original order. Don't worry about printing the list neatly; just print it as a raw Python list.
# Use sorted() to print your list in alphabetical order without modifying the actual list.
# Show that your list is still in its original order by printing it.
# Use sorted () to print your list in reverse-alphabetical order without changing the order of the original list.
# Show that your list is still in its original order by printing it again.
# Use reverse() to change the order of your list. Print the list to show that its order has changed.
# Use reverse() to change the order of your list again. Print the list to show it's back to its original order.
# Use sort() to change your list so it's stored in alphabetical order. Print the list to show that its order has been changed.
# Use sort() to change your list so it's stored in reverse-alphabetical order. Print the list to show that its order has changed.
places = ['cali', 'antarctica', 'alaska', 'europe', 'germany']
print(places)
print(sorted(places))
print(f'Still in its original order:')
print(places)
sorted_places = sorted(places, reverse=True)
print(sorted_places)
print(places)

places.reverse()
print(places)
places.reverse()
print(places)

places.sort()
print(places)
places.sort(reverse=True)
print(places)

#print(places[5]) # purposely get an IndexError
print(places[4])
print(places[-1])
print(places[3])
print(places[2])
