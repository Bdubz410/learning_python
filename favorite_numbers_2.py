# Modify your program from exercise 6-2 page 98 so each person can have more than one favorite number.
# Then print each person's name along with their favorite numbers.
favorite_numbers = {
    'brittany': [11, 27],
    'sue': [27, 11],
    'kaeden': [8, 15],
    'tiph': [7, 14],
    'britt': [1, 13],
    }

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for num in numbers:
        print(f"{num}")