# Make a dictionary called cities. Use the names of three cities as keys in your dictionary.
# Create a dictionary of information about each city and include the country that the city is in,
# its approximate population, and one fact about that city.
# The keys for each city's dictionary should be something like country, population, and fact.
# Print the name of each city and all the information you have stored about it.
cities = {
    'orlando': {
        'country': 'usa',
        'population': '2.7 million',
        'fact': 'Lake Eola is a sinkhole',
    },
    'chicago': {
        'country': 'usa',
        'population': '2.7 million',
        'fact': 'The L is the first elevated railway',
    },
    'denver': {
        'country': 'usa',
        'population': '2.9 million',
        'fact': 'The Mile High City',
    },
}

for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']

    print(f"\tIs in the {country.upper()}")
    print(f"\tThe population is approx {population}")
    print(f"\tA fun fact about the city: {fact}!")