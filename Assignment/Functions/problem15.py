# 15. Write a Python program to filter a list of integers using Lambda.

sample_list= [1,2,3,4,5,6,7,8,9]

#even filter
even_no= list(filter(lambda x:x%2==0, sample_list))
print("Even numbers are: ", even_no)

#odd filter 
odd_no= list(filter(lambda x:x%2!=0, sample_list))
print("Odd numbers are ", odd_no)

