# You don't have to limit the number of tests you create to 10.
# If you want to try more comparisons, write more tests and add them to conditional_tests.py
# Have at least one True and one False result for each of the following:
# Tests for equality and inequality with strings
# Tests using the lower() method
# Numerical tests involving equality and inequality, greater than and less than,
# greater than or equal to, and less than or equal to.
# Tests using the 'and' keyword and the 'or' keyword
# Test whether an item is in a list
# Test whether an item is not in a list

# my_car = 'subaru'
# my_car == 'bmw'  # False

# my_car.lower() == 'SUBARU'  # True
# my_car.lower() == 'Subaru'  # True

# babes_car = 'Crosstrek'
# babes_car != 'Impreza'  # True

# babes_car.title() != 'crosstrek'  # True
# babes_car.title() != 'Crosstrek'  # False

# numerical = 25
# numerical == 25  # True
# numerical != 25  # False

# numerical >= 75  # False
# numerical >= 100  # False
# numerical <= 83  # True
# numerical <= 1  # False
# numerical <= 25  # True
# numerical >= 25  # True

# stat_0 = 85
# stat_1 = 94

# stat_0 >= 22 and stat_1 >= 22   # True
# stat_0 <= 69 and stat_1 <= 99  # False

# stat_0 <= 75 or stat_1 <= 75   # False
# stat_0 >= 85 or stat_1 <= 85   # True

# **TERMINAL**

# my_list = ['coffee', 'sweater', 'hat', 'girlfriend']
# 'mushrooms' in my_list  # False
# 'backpack' in my_list  # False
# 'coffee' in my_list  # True
# 'girlfriend' in my_list  # True

not_invited = ['Jason', 'Monster', 'Sasha', 'Cayden']
rsvp = 'Kaeden'
if rsvp not in not_invited:
    print(f"{rsvp}, you are formally invited to my pool party!")