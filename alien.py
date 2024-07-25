# Simple dictionary

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# Accessing values in a dictionary
alien_0 = {'color' : 'green'}

print(alien_0['color'])

alien_0 = {'color': 'green', 'points': 5}
# If a player shoots down this alien, you can look up how many points they should earn using code like this:
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# Adding new key-value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an empty dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Modifying values in a dictionary
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien has evolved to {alien_0['color']}.")

# For a more interesting example: let's track the position of an alien
# that can move at different speeds. First store t=a value representing the alien's
# current speed and then use it to determine how far to the right the alien should move.
alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
print(f"Original position: {alien_0['x_position']}")

# Turned this alien into a fast one
alien_0['speed'] = 'fast'

# Move the alien to the right
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

# Removing key-value pairs using the del statement
# By providing the dict name and key with del it will permanently remove that key-value pair.
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)