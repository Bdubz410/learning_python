# Make a dictionary called favorite_places.
# Think of three names to use as keys in the dictionary, and store one to three favorite places for each person.
# Loop through the dictionary, and print each person's name and their favorite places.
favorite_places = {
    'britt': ['mountains', 'home'],
    'kaeden': ['santa fe', 'with me'],
    'tiphany': ['church'],
}

for person, places in favorite_places.items():
    print(f"\n{person.title()}'s favorite places are: ")
    if len(places) == 1:
        print(f"{places[0].title()}")
    else:
        for place in places:
            print(f"{place.title()}")