# Write a Python program to create a lambda function that adds 15 to a given
# number passed in as an argument, also create a lambda function that multiplies
# argument x with argument y and print the result.

lambda_function= lambda x:x+15

inp_num= int(input("Enter the number"))
print(lambda_function(inp_num))