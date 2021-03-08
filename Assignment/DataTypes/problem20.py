#  Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given list of
# strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

sample_list= ['abc', 'xyz', 'aba', 'apple', '1221']
count=1
for items in sample_list:
    if len(sample_list) and items[0]==items[-1]:
        count+=1
 
print(count)