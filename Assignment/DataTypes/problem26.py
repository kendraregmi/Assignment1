# Write a Python program to insert a given string at the beginning of all items in
# a list.
# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']

sample_list= [1,2,3,4]
str1= "emp"
print(['emp{0}'.format(i) for i in  sample_list])

