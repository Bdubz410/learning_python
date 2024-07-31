# Storing Your Functions in Modules
# You can store your function in a separate file called a module, then we can import that module into your main program.
# An import statement tells Python to make the code in a module available in the currently running program file.
# This allows you to hide the details of your program's code and focus on its higher-level logic.
# Importing an Entire Module
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")