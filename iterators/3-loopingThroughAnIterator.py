# Looping  through an iterator
# We can also use a for loop to iterate though an iterable object:

# Example 
# Iterate the values of a tuple:
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
    print(x)



# Example
# Iterate the characters of a string:
mystr = "banana"
for x in mystr:
    print(x)

# The for loop actually creates an iterator object and executes the next() method for each loop.