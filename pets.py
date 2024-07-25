# Make several dictionaries, where each dictionary represents a different pet.
# In each dictionary, include the kind of animal and the owner's name.
# Store these dictionaries in a list called pets.
# Next, loop through your list and as you do, print everything you know about each pet.
luna = {'animal': 'old english sheep', 'owner': 'kaeden'}

leo = {'animal': 'old english mix', 'owner': 'kaeden'}

johnny = {'animal': 'maine coon mix', 'owner': 'bdubz'}

pets = [johnny, leo, luna]
for pet in pets:
    print(f"Type of animal: {pet['animal'].title()}\t")
    print(f"The owner is {pet['owner'].title()} but we co-parent!")