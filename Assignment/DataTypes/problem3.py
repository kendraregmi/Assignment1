# 3. Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

input_string= input("Enter the string")
first_char= input_string[0]
print(first_char)
for letter in input_string:
    # if input_string.index > 0:
        if letter== first_char:
            first_char="$"
print(input_string)
            