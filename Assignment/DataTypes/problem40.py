# 40. Write a Python program to add an item in a tuple.

tuple1= (1, "Bob", "Kathmandu")
add_item= input(" Insert the item to add in tuple: ")
tuple2= (add_item,)
print(type(tuple2))
new_tuple= tuple1+tuple2
print(new_tuple)