# Write a Python program to remove the nthindex character from a nonempty
# string.

inp_str= input("Enter the string")
inp_index= int(input("Enter the position of the character to remove"))

new_string1= inp_str[:inp_index]
new_string2= inp_str[inp_index+1:]
new_string= new_string1+new_string2
print(new_string)

