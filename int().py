# Using int() to accept numerical input
# ** USE IN THE TERMINAL**

#age = input("How old are you? ")
# **TERMINAL**
#age
# Terminal will output the input to the question above but it will give it as a string ex: '21'

# Using int(): will do the following in the **TERMINAL**
#age = input("How old are you? ")
# How old are you? 21
#age >= 18
# Once all of this is in the Terminal we will experience an error due to Python reading the input as a string.
# Because Python cannot compare a string to an integer.

# Allowing the comparison to run without an error
#age = input("How old are you? ")
# How old are you? 21
#age = int(age)
#age >= 18
# True

age = input("How old are you? ")
age = int(age)

if age >= 18:
    print("You are all grown up!")
else:
    print("Stop growing up so fast!")