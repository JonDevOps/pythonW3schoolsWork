# Convert from Python to JSON
# # If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

# Example
# Convert from Python to JSON:
import json

# a Python object (dict):
x = {
    "name": "Jonathan",
    "age": 30,
    "city": "West Palm Beach"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

"""
YOu can convert Python objects of the following types, into JSON strings:
dict
list
tuple
string
int
float
true
false
none
"""

# Example
# Convert Python objects into JSONstringa, and print the values:
import json
print(json.dumps({"name": "Jonathan", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


"""
When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

Python - JSON
dict   - Object
list   - Array
tuple  - Array
str    - String
int    - Number
float  - Number
True   - true
False  - False
None   - null
"""

# Example
# Convert a Python object containing all the legal data types:
import json

x = {
    "name": "Jonathan",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))
