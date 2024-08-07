# Start with your class from restaurant.py.
# Create three different instances from the class, and call describe_restaurant() for each instance.
class Restaurant:
    """Describe a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize an establishment and the type of food."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Name the place and the cuisine served."""
        print(f"\nRestaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        """Indicate if the restaurant is open."""
        print(f"\n{self.restaurant_name}We are now open")


my_favorite = Restaurant('Snooze', 'Brunch')
her_favorite = Restaurant('Any place with', 'Thai Food')
their_favorite = Restaurant('Red Lobster', 'Seafood')

my_favorite.describe_restaurant()
her_favorite.describe_restaurant()
their_favorite.describe_restaurant()