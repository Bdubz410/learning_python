# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
# As they enter each topping, print a message saying you'll add that topping to their pizza.
prompt = "\nEnter your favorite pizza toppings:"
prompt += "\nWhen you are finished enter 'quit'. "

active = True
while active:
    toppings = input(prompt)

    if toppings == 'quit':
        break
    else:
        print(f"I will add {toppings} to your pizza!")