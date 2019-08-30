# Using the dir() function
# There is a built-in function to list all the function names (or variable name) in a module. The dir() function:

# Example
# List all the defined names belonging to the platfoorm module:
import platform

x = dir(platform)
print(x)

# Note: The dir() function can be used on all modules, also the onces you create yourself.