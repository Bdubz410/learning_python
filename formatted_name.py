# A function doesn't always have to display its output directly.
# Instead it can process some data and then return a value or set of values.
# A return value is the value the function returns.
# The return statement takes a value from inside a function and sends it back to the line that called the function.
# Return values allow you to move much of your program's grunt work into functions.

# Returning a Simple Value
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# When calling a function that returns a value, you need to provide a variable that the return value can be assigned to.
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Making an Argument Optional
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name =f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# To make the previous code with an optional argument we must assign an empty default value to a parameter.
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)