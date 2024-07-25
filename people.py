# Start with the program you wrote for exercise 6-1 page 98. Make two new dictionaries representing different people,
# and store all three dictionaries in a list called people.
# Loop through your list of people. As you loop through the list, print everything you know about each person.
my_love = {
    'first_name': 'kaeden',
    'last_name': 'primavera',
    'age': 34,
    'city': 'longmont',
}

me = {
    'first_name': 'bdubz',
    'last_name': 'wiederhold',
    'age': 35,
    'city': 'longmont',
}

sissy = {
    'first_name': 'tiph',
    'last_name': 'kankanala',
    'age': 39,
    'city': 'valparaiso'
}

people = [my_love, me, sissy]
for person in people:
    print(f"Name: {person['first_name'].title()} {person['last_name'].title()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].title()}\n")