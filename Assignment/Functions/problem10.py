# Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]


def even_no(sample_list):
    for items in sample_list:
        if items%2==0:
            print(sample_list[items])


sample_list= [1,2,3,4,5,6,7,8,9]
even_no(sample_list)