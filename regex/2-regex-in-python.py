# RegEx in Python
# When you have imported the re module, you can start using reegular expressions:

# Example
# Search the string to see if it starts with "The" and ends with "Spain":

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if (x):
    print ("YES! We have a match!")
else:
    print("No match")