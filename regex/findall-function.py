# The findall() Function
# The  findall() function returns a list containing all matches.

# Example
# Print a list of all matches.

import re

str = "The rain in Spain"
x = re.findall("ai", str)
print(x)