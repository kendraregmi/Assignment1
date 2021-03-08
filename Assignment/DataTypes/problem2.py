# 2. Write a Python program to get a string made of the first 2 and the last 2 chars
# from a given a string. If the string length is less than 2, return instead of the
# empty string.
# Sample String : 'Python'
# Expected Result : 'Pyon'
# Sample String : 'Py'
# Expected Result : 'PyPy'
# Sample String : ' w'
# Expected Result : Empty String

input_str= input("Enter the string ")
string_lenth= len(input_str)
if string_lenth>=3:
    new_string= input_str[0]+input_str[1]+input_str[-2]+input_str[-1]
    print("The new string is ",new_string)
elif string_lenth==2:
    new_string= input_str*2
    print("The new string is ",new_string)
else:
    new_string= "Empty String"
    print("The new string is ",new_string)