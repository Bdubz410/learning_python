# Turn your if-else chain from exercise 5-4 into an if-elif-else chain.
# If the alien is green, print a message that the player earned 5 points.
# If the alien is yellow, print a message that the player earned 10 points.
# If the alien is red, print a message that the player earned 15 points.
# Write three versions of this program, making sure each message is printed for the appropriate color alien.

alien_color = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
elif alien_color == 'red':
    print("You earned 15 points!")
else:
    print("Your alien color is not worthy of points!")

alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
elif alien_color == 'red':
    print("You just earned 15 points!")
else:
    print("No color for you!")

alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
elif alien_color == 'red':
    print("You just earned 15 points!")
else:
    print("No POINT for you!!")


alien_colors = 'green', 'yellow', 'red'

if 'green' in alien_colors:
    print("You just earned 5 points!")
elif 'yellow' in alien_colors:
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

if 'blue' in alien_colors:
    print("You just earned 5 points!")
elif 'yellow' in alien_colors:
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

if 'purple' in alien_colors:
    print("You just earned 5 points!")
elif 'black' in alien_colors:
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

