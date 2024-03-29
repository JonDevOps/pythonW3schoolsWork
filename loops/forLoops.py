"""
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
This is less like the for keyword in other programming languages, and more like an iterator method as found in other object-orientated programming langugages.
With the for loop we can execute a set of statements, once for each item in a list, tuple, set, etc.
"""

# Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


# Loop through the letters in the word "banana":
for x in "banana":
    print(x)


# Exit the loop when x is "banana": 
# Banana  will be printed in this loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break


# Exit the  loop when x is "banana", but this time the break comes before the print:
# Banana  will NOT be printed in this loop
fruits = ["apples", "banana", "cherry"]
for x in fruits:
        if x == "banana":
            break
        print(x)


# To loop through a set of  code a specified number of times, we can use the range() function.
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1(by default), and ends at a specified number.
for x in range(6): # Note that range(6) is not the values 0 to 6, but the values 0 to 5.
    print(x)

# The range()  function  defaults to 0 as a starting value, however it is possible to specify the starting value   by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
for x in range(2, 6):
    print(x)

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
for x in range(2, 30, 3):
    print(x)


# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
### Example - Print all numbers from 0 to 5. and print a message when the loop has ended:
for x in range(0, 6):
    print(x)
else:
    print("Finally  finished!")


# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":
# Example - Print each adjective for every fruit
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
