# Parse JSON - Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.
# The result will be a python dictionary

# Example
# Convert from JSON to Python:

import json

# some JSON
x = '{"name":"Jonathan", "age":30, "city":"West Palm Beach"}'

# parse x (i.e. convert from json to):
y = json.loads(x)

# the result is a python dictionary:
print(y["age"])