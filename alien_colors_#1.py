# Imagine an alien was just shot down in a game. Create a variable called alien_color
# and assign it a value of 'green', 'yellow', and 'red'.
# Write an if statement to test whether the alien's color is green.
# If it is, print a message that the player just earned 5 points.
# Write one version of this program that passes the if test and another that fails.

alien_color = 'green', 'yellow', 'red'

if 'green' in alien_color:
    print("You just earned 5 points!!")

if 'blue' in alien_color:
    print("You just lost!")