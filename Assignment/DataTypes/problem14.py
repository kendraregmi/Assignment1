# Write a Python function to create the HTML string with tags around the
# word(s).
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'

def add_tags(tag, my_string):
    print( f'<{tag}> {my_string} <{tag}>')


add_tags("i", "Python")
add_tags("b", "Python Tutorial")
