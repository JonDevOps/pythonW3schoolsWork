# The split() Function returns a list where the string has been split at each match:

# Example
# Split at each white spaced character:
"""
# Uncomment to see code

import re

str = "The rain in Spain"
x = re.split("\s", str)
print(x)
"""

# You can control the number of occurences by specifying the maxsplit parameter:




# Example
# Split the string only at the first occurence:

import re

str = "The rain is in Spain"
x = re.split("\s", str, 1)
print(x)