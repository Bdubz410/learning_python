# Checking Whether a Value Is in the List
# To find out if a particular value is already in a list, use the keyword 'in'

# Test in TERMINAL
# requested_toppings = ['mushrooms', 'onions', 'pineapple']
# 'mushrooms' in requested_toppings
# True

# 'pepperoni' in requested_toppings
# False

# Checking Whether a Value Is Not in a List using the keyword 'not'

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# Boolean Expressions is just another name for conditional test
# A boolean value is either True or False, just like the value of a conditional expression after evaluation
# Boolean values provide an efficient way to track the state of a program or a particular condition  that is important in your program
