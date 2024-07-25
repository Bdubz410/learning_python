# Start your program from exercise 4-1 on page 56. Make a copy of the list of pizzas, and call it friend_pizzas. Then do the following:
# Add a new pizza to the original list.
# Add a different pizza to the list friend_pizzas
# Prove that you have two separate lists. Print the message My favorite pizzas are:," and then use a for loop to print the first list.
# Print the message "My friend's favorite pizzas are:," and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.

pizzas = ['pineapple', 'pepperoni', 'jalapeno', 'green pepper']
friend_pizzas = pizzas[:]

print(friend_pizzas)

pizzas.append('basil')
friend_pizzas.append('anchovy')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)