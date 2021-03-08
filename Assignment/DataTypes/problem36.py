# 36. Write a Python program to sum all the items in a dictionary.

new_dict= {1:1, 2:4, 3:9, 4:16, 5:25, 8:64}
values=0
for i in new_dict:
    values+= new_dict[i]
print("Sum of items is: ", values)