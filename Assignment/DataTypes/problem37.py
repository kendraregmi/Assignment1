# 37. Write a Python program to multiply all the items in a dictionary.

my_dict = {'a':3000,'b':700,'c':54}
result=1
for key in my_dict:    
    result=result * my_dict[key]

print("Multiplication is" ,result)