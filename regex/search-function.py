# The search() function
# The search() function searches the string for a match, and returns a Match object if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned:

# Example
# Search for the first white-space character in the string:
import re

str = "The rain in Spain"
x = re.search("\s", str)

print("The first white-space character is located in position:", x.start())


# If no matches are founnd, the value NOne is returned:

# Example
# Make a search that returns no match:

import re 

str = "The rain is in Spain"
x = re.search("Portugal", str)
print(x)