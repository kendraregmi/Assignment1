# Write a Python program to add 'ing' at the end of a given string (length should
# be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
# string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

def ly_add_funct(given_string):
    suffix= 'ing'
    if given_string.endswith(suffix):
        given_string+="ly"
    else:
        given_string+="ing"
    print(given_string)

given_string= input("Input the string: ")
if len(given_string)<3:
    print(given_string)
else:
    ly_add_funct(given_string)


