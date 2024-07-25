# Using if Statements with Lists
# Checking for Special Items

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}")

print("\nFinished making your pizza!")

# Checking That a List is Not Empty.
requested_toppings = []

if requested_toppings:   # Python returns True if the list contains at least one item; an empty list evaluates to False.
    for requested_topping in requested_toppings:   # If requested_toppings passes the conditional test then the for loop will run
        print(f"Adding {requested_topping}.")   # If it fails Python skips the for loop and runs the else statement.
    print("\nFinished making your pizza!")
else:
    print("\nAre you sure you want a plain pizza?")

# Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")