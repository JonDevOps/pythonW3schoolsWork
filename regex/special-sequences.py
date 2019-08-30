# Special Sequences
# A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

"""
Character - Description                         -                       Example     -   Try it
\A          Returns a match if the specified characters are             "[a-m]"         import re    
            at the beginning of the string                                              str = "The rain in Spain"
                                                                                        #Check if the string starts with "The":
                                                                                        x = re.findall("\AThe", str)
                                                                                        print(x)
                                                                                        if(x)
                                                                                            print("Yes, there is a match!")
                                                                                        else:
                                                                                            print("No match")

\b

\B

\d

\D

\s

\S

\w

\W

\Z

"""