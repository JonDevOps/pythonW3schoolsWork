# Format the Result
# the example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
# The json.dumps() method has parameters to make it easier to read the result:

# Example
# Use the indent parameter to define the numbers of indents:

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

print(json.dumps(x, indent=4))

# You can also define the seperators, default value is (",",":"), which means using a comma and a space to seperate each object, and a colon and a space to seperate keys from values:

""""
Heres an example how 
# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
Use the separators parameter to change the default separator:
print(json.dumps(x, indent=4, separators=(". ", " = ")))
"""

# Order the result
# The json.dumps() method has parameters to order the keys in the result:

# Example
# Use the sort_keys parameter to specify if the result should be sorted or not:
"""
 json.dumps(x, indent=4, sort_keys=True)
"""