# The strftime method
# The datetime object has a method for formatting dat objects into readable strings.
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string.

# Example
# Display the time of the month:
import datetime 
x = datetime.datetime(2018, 6, 1)

print(x.strftime("%A"))