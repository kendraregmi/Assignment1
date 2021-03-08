# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

def sum_all(*num):
    sum=0
    for n in num:
        sum=sum+n
    return sum

print(sum_all(8,2,3,0,7))