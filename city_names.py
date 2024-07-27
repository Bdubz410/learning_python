# Write a function called city_country() that takes in the name of a city and its country.
# The function should return a string formatted like this: "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the values that are returned.
def city_country(city, country):
    """Name a City and its Country."""
    place = f"{city}, {country}"
    return place.title()

p_lace = city_country('paris', 'france')
print(p_lace)

p_lace = city_country('tokyo', 'japan')
print(p_lace)

p_lace = city_country('sydney', 'australia')
print(p_lace)