# Numerical Comparisons

# Testing numerical values is pretty straightforward
# Example in TERMINAL

# age = 18    # This is asking whether a person is 18 years old
# age == 18
# True

# Test to see if two numbers are not equal
# For example the following code prints a message if the given answer is not correct

answer = 17
if answer != 42:    # The conditional test passes because the value of answer (17) is not equal to 42
    print("That is not the correct answer. Please try again!")

# You can include various mathematical comparisons in your conditional statements as well.
# Example in TERMINAL
# age = 19
# age < 21
# True

# age <= 21
# True

# age >= 21
# False

# age >= 21
# False
# Each mathematical comparison can be used as part of an if statement, which can help you detect the exact conditions of interest.

# Checking Multiple Conditions Using and

# age_0 = 22
# age_1 = 18
# age_0 >= 21 and age_1 >= 21   # This is False because both conditions are not True so the conditional expression is False
# False

# age_0 = 22  # Changed the value to allow a True outcome.
# (age_0 >= 21) and (age_1 >= 21)   # Can use parenthesis around the individual tests, for readability, but they are not required.
# True

# Using or to Check Multiple Conditions

# age_0 = 22
# age_1 = 18
# age_0 >= 21 or age_1 >=21
# True

# age_0 = 18   # Changed the value of the variable
# age_0 >= 21 or age_1 >= 21
# False