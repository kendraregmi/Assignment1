#  Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

sentence= input("Enter the string")
not_string= sentence.find("not")
poor_string= sentence.find("poor")

if poor_string>not_string:
    sentence= sentence.replace(sentence[not_string:(poor_string+4)], "good")
    print(sentence)
else:
    print(sentence)

