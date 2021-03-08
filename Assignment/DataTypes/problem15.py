# Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}

def add_in_middle(string_in, string_btn):
    middle_index= int(len(string_in)/2)
    print(string_in[:middle_index]+string_btn+string_in[-middle_index:] )

string_in= input("Enter the string: ")
string_middle= input("Enter the string to add in middle: ")
add_in_middle(string_in, string_middle)