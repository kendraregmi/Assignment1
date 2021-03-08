# 8. Write a Python function that takes a list and returns a new list with unique
# elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]


def unique_list(sample_list):
    new_set= set(sample_list)
    sample_list= list(new_set)
    print(sample_list, type(sample_list))


sample_list= [1,2,3,3,3,3,4,5]
unique_list(sample_list)