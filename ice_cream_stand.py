# An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the
# Restaurant class from page 162 or page 166. Either version of the class will work; just pick the one you like better.
# Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors.
# Create an instance of IceCreamStand, and call this method.
class Restaurant:
    """Describe a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Name the establishment and the type of food."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\nRestaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        """Indicate if the restaurant is open."""
        print(f"\n{self.restaurant_name} is now open")

    def set_number_served(self, number):
        """Set the number of people served."""
        self.number_served = number

    def increment_number_served(self, number):
        """Increment the number of customers who've been served."""
        self.number_served += number


class IceCreamStand(Restaurant):
    """Represent an ice cream stand"""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes from the parent class.
        Then initialize attributes in a list specific to ice cream flavors.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'cookies N cream', 'strawberry']

    def describe_flavors(self):
        """Display the ice cream flavors."""
        print(f"The ice cream flavors available are: {self.flavors}!")


ice_cream = IceCreamStand('Baskin Robbins', 'ice cream')
ice_cream.describe_flavors()