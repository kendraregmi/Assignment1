# Write a Python script to generate and print a dictionary that contains a
# number (between 1 and n) in the form (x, x*x).

dict= {}
range_no= int(input("Enter the range: "))
i = 1

for i in range(1, range_no+1):
    dict[i]=i*i
print(dict)

