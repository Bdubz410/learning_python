# Looping through all key-value pairs in a few lines of code
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python,'
    }
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# Looping through all the keys in a dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python,'
    }

for name in favorite_languages.keys():
    print(name.title())
# Looping through the keys is default behavior when looping through a dictionary. So this code gives the same output.
for name in favorite_languages:
    print(name.title())

# You can access the value associated with any key you cate about inside the loop, by using the current key.
# Let's print a message to a couple of friends about the languages they chose.
# We'll loop through the names in the dictionary as we did previously.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python,'
    }
friends = ['phil', 'sarah']
for name in favorite_languages:
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
# We can also use the keys() method to find out if a particular person was polled.
if 'erin' not in favorite_languages:
    print("\nErin, please take our poll!")

# Looping through a dictionary's keys in a particular order.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python,'
    }

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Looping through all values in a dictionary.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python,'
    }

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# We will use set() to weed out any repeats
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python,'
    }

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())