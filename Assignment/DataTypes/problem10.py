# 10. Write a Python program to remove the characters which have odd index
# values of a given string.

my_string= "Kathmandu"
result=""
for i in range(len(my_string)):
    if i%2==0:
        result= result+my_string[i]

print(result)
