# Write a Python program to replace the last element in a list with another list.
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

sample_list= [1,3,5,7,9,10]
add_list=[2,4,6,8]
new_list= sample_list[0:-1]+add_list
print(new_list)