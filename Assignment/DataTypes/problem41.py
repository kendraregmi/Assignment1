# 41. Write a Python program to convert a tuple to a string.


tup1= ("Hello", 1, "namaste")
str2= "".join(tup1)

str1= tup1[0]+str(tup1[1])+tup1[2]
print(str1)
print(str2)