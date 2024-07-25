# Using the list sandwich_orders from exercise deli.py,
# make sure the sandwich 'pastrami' appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami,
# and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.
sandwich_orders = ['pastrami', 'ham', 'cheese', 'pastrami', 'grinder', 'pastrami', 'meatball']
finished_sandwiches = []

print("We are out of pastrami, sorry for the inconvenience!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"I made your {sandwich} sammie!")
    finished_sandwiches.append(sandwich)

print("\nFinished Sammies:")
for sammie in finished_sandwiches:
    print(f"{sammie.title()} sammie")