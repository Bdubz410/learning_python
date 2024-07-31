# Write a function that accepts a list of items a person wants on a sandwich.
# The function should have one parameter that collects as many items as the function call provides,
# and it should print a summary of the sandwich that's being ordered.
# Call the function three times, using a different number of arguments each time.
def make_sandwich(*fillings):
    """Print a list that makes a sandwich."""
    print(fillings)

make_sandwich('ham', 'pepperjack', 'turkey')
make_sandwich('peanut butter', 'jelly')
make_sandwich('gf bread', 'vegan cheese', 'marinara', 'meatballs')