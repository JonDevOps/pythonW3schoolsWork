# Sets
# A set is a set of characters inside a pair of square brackets [] with a special meaning:

"""
Set     -    Description                                -                                       Try it
[arn]       Returns a match where one of the specified characters (a, r, or n) are present      import re
                                                                                                str = "The rain in Spain"
                                                                                                # Check if the string has any a, r, or n characters:
                                                                                                x = re.findall("[arn}", str)
                                                                                                print(x)
                                                                                                if (x):
                                                                                                    print("Yes, there is at least one match!")
                                                                                                else:
                                                                                                    print("No match")


















"""