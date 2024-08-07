# Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name
# and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information,
# and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
class Restaurant:
    """Describe a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Name the establishment and the type of food."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nRestaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        """Indicate if the restaurant is open."""
        print(f"\n{restaurant.restaurant_name} is now open")


restaurant = Restaurant('Collision', 'Vegan')

print(f"My favorite restaurant is {restaurant.restaurant_name}.")
print(f"I like to indulge in {restaurant.cuisine_type} food there!")
restaurant.open_restaurant()
restaurant.describe_restaurant()