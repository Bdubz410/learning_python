# Object_oriented programming (OOP) is one of the most effective approaches to writing software.
# In OOP, you write classes that represent real-world things and situations,
# and you create objects based on these classes.
# When you write a class, you define the general behavior that a whole category of objects can have.
# Making an object from a class is called instantiations, and youi work with instances of a class.

# Creating and Using a Class
# Creating the Dog Class
# We capitalize names to refer to classes in Python
class Dog:
    """A simple attempt to model a dog."""

# A function that's part of a class is a method (init() method)
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        # The line self.name takes the value associated with the parameter 'name' and assigns it to the variable name,
        # which is then attached to the instance being created.
        # Variables that are accessible through instances like this are called attributes.
        self.name = name
        self.age = age

# The Dog class has two other methods sit() and roll_over(). Since these methods don't need additional info to run,
# we just define them to have one parameter, self.
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


# Making an Instance from a Class
# Think of a class as a set of instructions for how to make an instance.
my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old")

# Accessing Attributes: **NOTE** the following lines are discussing the previous code above.
# In order to access attributes of an instance, you use dot notation.
# We access the value of my_dog's attribute name by writing:
#my_dog.name
#my_dog.age

# Calling Methods
# After we create an instance from the class Dog, we can use dot notation to call any method defined in Dog.
# Let's make our dog sit and roll over:
my_dog.sit()
my_dog.roll_over()
# To call a method give the name of the instance (in this case my_dog) & the method you want to call, separated by a (.)

# Creating Multiple Instances
your_dog = Dog('Lucy', 3)

# In this example each dog is a separate instance with its own set of attributes, capable of the same set of actions.
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your do is {your_dog.age} years old.")
your_dog.sit()