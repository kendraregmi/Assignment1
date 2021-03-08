# Write a Python program to get a single string from two given strings, separated
# by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

given_string= input("Enter the new string of two words ")
string_list= given_string.split()
print(string_list)
string1= string_list[0]
string2= string_list[1]
print("First string is ", string1)
print("second string is ", string2)

new_string1= string1[:2]+string2 [2:]
new_string2= string2[:2]+string1[2:]
print ("The new strings are: ", new_string1, new_string2)
