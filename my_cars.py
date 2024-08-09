# Importing Multiple Classes from a Module
# You can import as many classes as you need into a program file.
from car_module import Car, ElectricCar

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_electric_car = ElectricCar('tesla', 'model s', 2024)
print(my_electric_car.get_descriptive_name())

# Importing an Entire Module
# You can import an entire module and then access the classes you need using dot notation.
# This approach is simple and results in code that is easy to read.
# Because every call that creates an instance of a class includes the module name, you won't have naming conflicts.
import car_module

my_mustang = car_module.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_electric_car = car_module.ElectricCar('tesla', 'model s', 2024)
print(my_electric_car.get_descriptive_name())

# Importing All Classes from a Module
# You can import every class from a module using the following syntax:
# from module_name import *
# The above syntax is not recommended for several reasons: there can be naming conflicts, you cannot read the import
# statements at the top of the file which can be helpful to get a clear sense of which classes the program is using.
# Best Practices is to import the whole module then use the dot notation .

# Importing a Module into a Module (from electric_car_module.py)
# Now we can import from each module separately and create whatever kind of car we need.
# Example from .py files car_module_new and electric_car_module)
from car_module_new import Car
from electric_car_module import ElectricCar

my_subaru = Car('subaru', 'crosstrek', 2024)
print(my_subaru.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2024)
print(my_tesla.get_descriptive_name())