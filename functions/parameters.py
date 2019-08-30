# Information can be passed to a function as a parameter
# Parameters are specified after the function name, inside the parenthesis. You can add as many parameters as you want, just seperate them with a comma.
# The following example has a function with on parameter (fname.) When the function is called, we pass along a first name, which is used inside the function to print the full name.

def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

