# Write a Python function that takes a list of words and returns the length of the
# longest one.

def max_length(sentencelist):
    maximum_is= 0
    for i in sentencelist:
        if len(i)>maximum_is:
            maximum_is= len(i)
    print(maximum_is)

sentence= input("Enter the sentence")
sentencelist= sentence.split()
max_length(sentencelist)


