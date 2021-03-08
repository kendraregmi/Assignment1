# Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
 

def str_no(inp_str):
    upper_no= 0
    lower_no= 0
    for c in inp_str:
        if c.isupper():
            upper_no+=1
        elif c.islower():
            lower_no+=1
        else:
            pass
    print("No. of upper char:", upper_no, "and lower char:", lower_no)
inp_str= input("Enter the string")
str_no(inp_str)





