# Start with your program from page 162 (Restaurant). Add an attribute called number_served with a default value of 0.
# Create an instance called restaurant from this class.
# Print the number of customers the restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number of customers that have been served.
# Call this method with a new number and print the value again.
# Add a method called increment_number_served() that lets you increment the number of customers who've been served.
# Call this method with any # you like that could represent how many customers were served in, say, a day of business.
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


restaurant = Restaurant("Chili's", 'American', )
restaurant.describe_restaurant()

print(f"Number of customers served: {restaurant.number_served}")

restaurant.number_served = 35
print(f"Number of customers served: {restaurant.number_served}")

restaurant.set_number_served(50)
print(f"Number of customers served: {restaurant.number_served}")

restaurant.increment_number_served(315)
print(f"Number of customers served in the day: {restaurant.number_served}")