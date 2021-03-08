#  Write a Python program to create a function that takes one argument, and
# that argument will be multiplied with an unknown given number.

def mul_func(inp_no):
    return lambda x:x*inp_no

res=mul_func(2)
print( "Double of num 15 is",res(15) )