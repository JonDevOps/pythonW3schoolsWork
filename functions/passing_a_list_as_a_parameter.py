# You can send any data types of parameter to a function (string, number, list, dictionary etc.)
# E. G. if you send a List as a parameter, it will still be a List when it reaches the function:

def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)