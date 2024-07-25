# The is-elif-else Chain

age = 12

if age < 4:
    print("Your admission is $0.")
elif age < 18:
    print("Your admission is $25.")
else:
    print("Your admission is $40.")

# Instead of placing the price in the block
# It would be easier to place it in the chain
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")   # This revised code is much cleaner and easier to edit

# Using Multiple elif Blocks
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20   # This block added for ages over 65 at $20

print(f"Your admission cost is ${price}.")

# Omitting the else Block
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")

print("Kaeden I love you baby!!!")