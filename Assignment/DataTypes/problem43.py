# 43. Write a Python program to remove an item from a tuple.

my_tup= ("hi", "this", "is","new","tuple", "Example")
#removing the last element
new_tup= my_tup[:5]
print(new_tup)
print(type(my_tup))

#removing from middle index, using slicing and +
new_tup1= my_tup[:3]+ my_tup[-2:]
print(new_tup1)