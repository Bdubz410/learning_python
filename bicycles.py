# Practicing working with lists

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Accessing elements in a list
print(bicycles[0])
print(bicycles[0].title())

# Index positions start at 0 not 1
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])  # -1 displays the last item in a list, -2 the second to last item, and so on.

# Using individual values from a list
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)