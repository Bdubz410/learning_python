# Storing Multiple Classes in a Module
# Add the Battery and ElectricCar classes to car_module.py.
# You can store as many classes as you need in a single module, although each class should be related somehow.
# Now we will import the ElectricCar class and make an electric car.
from car_module import ElectricCar

my_electric_car = ElectricCar('tesla', 'model s', 2024)
print(my_electric_car.get_descriptive_name())
my_electric_car.battery.describe_battery()
my_electric_car.battery.get_range()