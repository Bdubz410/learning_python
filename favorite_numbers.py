# Use a dictionary to store people's favorite numbers.
# Think of five names, and use them as keys in your dictionary.
# Think of a favorite number for each person, and store each as a value in your dictionary.
# Print each person's name and their favorite number.
favorite_numbers = {
    'brittany': 11,
    'sue': 27,
    'kaeden': 7,
    'tiph': 3,
    'britt': 13
    }
for name, number in favorite_numbers.items():
    print(f"{name.title()}'s favorite number is {number}!")

num = favorite_numbers['brittany']
print(f"Brittany's favorite number is {num}.")
num = favorite_numbers['sue']
print(f"Sue's favorite number is {num}.")
num = favorite_numbers['kaeden']
print(f"Kaeden's favorite number is {num}.")
num = favorite_numbers['tiph']
print(f"Tiph's favorite number is {num}.")
num = favorite_numbers['britt']
print(f"Britt's favorite number is {num}.")