# Match Object
# A match Object is an object containing information about the search and the result.
# Note: If there is no match, the value None will be returned, instead of the Match Object.

# Example
# Do a search that will return a Match Object:
"""
# Uncomment this code to test this example

import re

# The search() function returns a Match Object:

str = "The rain in Spain"
x = re.search("ai", str)
print(x) # This will print an object
"""


"""
The Match object has properties and methods used to retrieve information about the search, and the result:
.span() returns a tuple containing the start-, and end positions of the match.
.string() returns the string passed into the function
.group() returns the part of the string where there was a match
"""


# Example
# Print the position (start- and end-position) of the first match occurence.
# The regular expression looks for any words that starts with an uppercase "S":
"""
import re

str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.span())
"""


# Example 
# Print the string tpassed into the function:
"""
# Uncomment to see the code
import re

str = "The rain is in Spain"
x = re.search(r"\bS\w+", str)
print(x.string)
"""


# Example
# Print the part of the string where there was a match.
# The regular expression looks for any words that starts with an upper case "S":

# Uncomment to see the code
import re
str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.group())