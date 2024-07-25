# rstrip() method

favorite_language = "python "
print(favorite_language)
print(favorite_language.rstrip())  # **RUN IN TERMINAL**

favorite_language = 'python '
favorite_language = favorite_language.rstrip()  # Associate new value with original variable to also remove whitespace from the right
print(favorite_language)  # **RUN IN TERMINAL**

favorite_language = ' python '
favorite_language.rstrip()  # Strips whitespace from the right
favorite_language.lstrip()  # Strips whitespace from the left
favorite_language.strip()  #  Strips whitespace from both sides