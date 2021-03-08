# 22. Write a Python program to remove duplicates from a list.

my_list= [12,34,2,56,23,12,67,76]
my_set= set(my_list)
my_list=list(my_set)
print("Duplicate removed list is",my_list, type(my_list) )

