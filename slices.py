# Using one of the programs you wrote in this chapter,
# add several lines to the end of the program that do the following:
# Print the message "The first three items in the list are:."
# Then use a slice to print the first three items from that program's list.
# Print the message "Three items from the middle of the list are:."
# Then use a slice to print three items from the middle of the list.
# Print the message " The last three items in the list are:." Then use a slice to prin the last three items in the list.

archer_characters = ['archer', 'lana', 'malory', 'pam', 'cyril', 'carol']

print("The first three characters in the list are:")
for char in archer_characters[:3]:
    print(char.title())

print("\nThree characters from the middle of the list are:")
for char in archer_characters[1:4]:
    print(char.title())

print("\nThe last three characters in the list are:")
for char in archer_characters[-3:]:
    print(char.title())
