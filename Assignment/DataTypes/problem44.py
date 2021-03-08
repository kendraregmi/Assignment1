# 44. Write a Python program to slice a tuple.

my_tup= ("hi", "this", "is","new","tuple", "Example")
#slicing the last element
new_tup= my_tup[:5]
print(new_tup)
print(type(my_tup))

#slicing from middle and removing one element
new_tup1= my_tup[:3]+ my_tup[-2:]
print(new_tup1)