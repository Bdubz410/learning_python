# Defining a function.
# def tells Python we are defining a function; greet_user() is the function definition which must end with ():
# any information after the : make up the body of the function.
# The text on the second line is a comment called a docstring, which describes what the function does.
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

# Passing information to a function.
# The variable username in the definition is an example of a parameter.
# The value 'jesse' is an example of an argument.
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')
greet_user('kaeden')
greet_user('bdubz')