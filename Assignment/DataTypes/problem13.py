# 13.Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically).

string_inp= input("Enter the word separated by commas: ")
my_list= string_inp.split(", ")
my_set= set(my_list)
print(sorted(my_set))

