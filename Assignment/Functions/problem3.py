# Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

def multiplier(*nums):
    mul=1
    for n in nums:
        mul*=n
    return mul

print(multiplier(8,2,3,-1,7))