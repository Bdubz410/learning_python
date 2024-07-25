# All versions of foods.py in this section have avoided using for loops when printing, to save space.
# Choose a version of foods.py, and write two for loops to print each list of foods.

my_foods = ['tiramisu', 'pizza', 'spicy']
friend_foods = my_foods[:]    # syntax for how to copy a list

my_foods.append('burgers')    # adding a food to my list
friend_foods.append('seafood')   # adding a food to my friend's list

print(my_foods)
print(friend_foods)

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)