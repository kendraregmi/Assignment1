# 11. Write a Python program to count the occurrences of each word in a given
# sentence.

my_string=input("Enter string:")
word=input("Enter word:")
a=[]
count=0
a=my_string.split(" ")
for i in range(0,len(a)):
      if(word==a[i]):
            count=count+1
print("Count of the word is:")
print(count)