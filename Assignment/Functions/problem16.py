# 6. Write a Python program to square and cube every number in a given list of
# integers using Lambda.

sample_list= [1,2,3,4,5,6,7,8,9]
#square no
sq_list= list(map(lambda x:x*x, sample_list))
print("square no of list is: ", sq_list)

#cube No
cu_list= list(map(lambda x:x*x*x, sample_list))
print("cube is",  cu_list)