# Variables in functions
# The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects, etc):

# Example
# Save this code in the file mymodule.py
person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}

# Example
# Import the module named mymodul, and access the person1 dictionary:
idef greeting(name):
    print("Hello, " + name)
def greeting(name):
    print("Hello, " + name)
mport mymodule
a = mymodule.person1["age"]
print(a)