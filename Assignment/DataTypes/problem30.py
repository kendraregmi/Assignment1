# 30. Write a Python script to check whether a given key already exists in a
# dictionary.

my_dict= {1:1, 2:4, 3:9, 4:16}
inp_key=1
if my_dict.get(inp_key)==True:
    print("Key avilable")
else:
    print ("Key not available")