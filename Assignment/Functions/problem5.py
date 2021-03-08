# 5. Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument

def fact(num):
    factorial= 1
    for a in range(1,num+1):
        factorial*=a
        a+=1
    return factorial

print(fact(5))
    
