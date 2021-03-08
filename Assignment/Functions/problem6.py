# 6. Write a Python function to check whether a number is in a given range.

def is_in_range(num, range_start, range_stop):
    if num in range(range_start,range_stop):
        print("Number is in range ")
    else:
        print("Not in range ")
    
range_start= int(input("Enter the start of range: "))
range_stop= int(input("Enter the end of the range: "))
num= int(input("Enter the number: "))
is_in_range(num, range_start, range_stop)