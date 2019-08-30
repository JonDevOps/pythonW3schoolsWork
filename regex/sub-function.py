# The sub() function
# The sub() function replaces the matches with the text of your choice:

# Example
# Replace every white-space character with the number 9:

import re

str = "The rain in Spain"
x = re.sub("\s", "9", str)
print(x)



# You can control the number of replacements by specifying the count parameter:

# Example
# Replace the first 2 occurences:
"""
import re

str = "The rain in Spain"
x = re.sub("\s", "9", str, 2)
print(x)
"""