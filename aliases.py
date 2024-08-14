# As with functions, aliases can be quite helpful when using modules to organize your projects' code.
# You can use aliases when importing classes as well.
# As an example, consider a program where you want to make a bunch of electric cars.
# It might get tedious to type (and read) ElectricCar over and over again.
# You can give ElectricCar and alias in the import statement:
from electric_car_module import ElectricCar as EC

# Now you can use this alias whenever you want to make an electric car:
my_tesla = EC('tesla', 'model s', 2024)
print(my_tesla.get_descriptive_name())

# You can also give a module an alias. Here's how to import the entire electric_car_module module using an alias:
import electric_car_module as ec

# Now youcan use this module alias with the full class name:
my_tesla = ec.ElectricCar('tesla', 'model s', 2024)
print(my_tesla.get_descriptive_name())