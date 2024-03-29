
#Inheritance allows us to define a class that inherits all the methods and properties from another class.
#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class, also called derived class.

# Create a parent class
# Any class can be a parent class, so the syntax is the same as creating any other class:

#Example
#Create a  class named Person with firstname and lastname properties, and a printname method

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

# Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()



# Create a child class
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class

# Example
# Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(Person):
    pass

# Note: Use the pass keyword when you do not want to add any other properties or methods to the class.

# Now the Student class has the same properties and methods as the Person class.

#Example
# Use the Student class to create an object, and then execute the printname method:
x = Student("Mike", "Olsen")
x.printname()



# Add the __init__() function
# So far we have cteated a child class that inherits the properties and methods from its parent.
# We want to add the __init__() function to the child class (instead of the pass keyword).
# Note: The __init__() function is called automacically every time the class is being used to create a new object.

# Example
# Add the __init__() function to the Student class:

"""
class Student(Person):
  def __init__(self, fname, lname):
    # add properties etc.
"""

#  When you  add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# Note: The child's __init__() function overides the inheritance of the parent's __init__() function.

# To keep the inheritance of the parent's  __init__() function, add a call to the parent's __init__() function:

# Example 

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

# Now we have successfully  added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality to the __init__() function.



# Add properties

# Example
# Add a property called graduationyear to the Student class:
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
    self.graduationyear = 2019

    x = Student("Mike", "Olsen")
    print(x.graduationyear)