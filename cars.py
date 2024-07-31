# Write a function that stores information about a car in a dictionary.
# The function should always receive a manufacturer and a model name.
# It should then accept an arbitrary number of keyword arguments.
# Call the function with the required info and two other name-value pairs, such as a color or an optional feature.
# Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that's returned to make sure all the information was stored correctly.
def make_car(manufacturer, model_name, **car_info):
    """Give a detailed description about a car."""
    car_info['make'] = manufacturer
    car_info['model'] = model_name
    return car_info

car = make_car('porsche', 'boxster',
               color='white',
               moon_roof=True)

print(car)