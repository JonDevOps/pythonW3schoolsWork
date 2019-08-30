# Metacharacters
# Metacharacters are characters with a special meaning:

"""
Character   -   Description                 -               Example     -    Try It
[]              A set of characters                         "[a-m]"         import re
                                                                            str = "The rain in Spain"
                                                                            # Find all lower case characters alphabetically between "a" and "m":
                                                                            x = re.findall("[a-m]", str)
                                                                            print(x)

\               Signals a special sequence (can also        "\d"            import re
                be used to escape special characters)                       str = "That will be 59 dollars"
                                                                            # Find all digit characters:
                                                                            x = re.findall("\d", str)
                                                                            print(x)

.               Any character (except newline character)    "he..o"         import re
                                                                            str = "hello world"
                                                                            # Search for a sequence that starts with the "he", followed by two (any) characters, and an "o":
                                                                            x = re.findall("he..o", str)
                                                                            print(x)

^               Starts with                                 "^hello"        import re
                                                                            str = "hello world"
                                                                            # Check if the string starts with 'hello':
                                                                            x = re.findall("^hello", str)
                                                                            if (x):
                                                                                print("Yes, the string starts with 'hello'")
                                                                            else:
                                                                                print("No match")

$               Ends with                                   "world$"        import re
                                                                            str = "hello world"
                                                                            # Check if the string ends with 'world':
                                                                            x = re.findall("world$", str)
                                                                            if (x):
                                                                                print("Yes, the string ends with 'world'")
                                                                            else:
                                                                                print("No match")               

*               Zero or more occurrences                    "aix"           import re
                                                                            str = "The rain in Spain falls mainly in the plain!"
                                                                            # Check if the string contains "ai" followed by 0 or more "x" characters:
                                                                            x = re.findall("aix*", str)
                                                                            print(x)
                                                                            if (x):
                                                                                print("Yes, there is at least one match!")
                                                                            else:
                                                                                print("No match")

+               One or more occurrences                     "aix+"          import re
                                                                            str = "The rain in Spain falls mainly in  the plain!"
                                                                            # Check if the string contains "ai" followed by 1 or more "x" characters:
                                                                            x = re.findall("aix+", str)
                                                                            print(x)
                                                                            if (x):
                                                                                print("Yes, there is at least one match!")
                                                                            else:
                                                                                print("No match") 

{}              Exactly the specified number of occurrences "al{2}"         import re
                                                                            str = "The rain in Spain falls mainly in the plain!"
                                                                            # Check if the string contains "a" followed by exactly two "l" characters:
                                                                            x = re.findall("al{2}", str)
                                                                            print(x)
                                                                            if (x):
                                                                                print("Yes, there is at least one match!")
                                                                            else:
                                                                                print("No match")

|               Either or                                   "al{2}"         import re
                                                                            str  = "The rain in Spain falls mainly in the plain!"
                                                                            # Check if thestring contains either "falls" or "stays":
                                                                            x = re.findall("falls|stays", str)
                                                                            print (x)
                                                                            if (x):
                                                                                print ("Yes, there is at least one match!")
                                                                            else:
                                                                                print("No match")

()              Capture and group                                       

"""