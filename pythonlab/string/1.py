#1. Write a Python program to count the occurrences of each word in a
#given sentence.
str1 = input("Enter a string: ")
searchstring = input("Enter a character or word to check its occurrnces :")
#count number of character
count = 0
for i in str1:
    if i == searchstring:
        count += 1
print("Number of Occurence :",count)
word = input("Enter a word :")
str2 = str1.split()
count = 0
for s in  str2:
    if s == word:
        count += 1
print("No of Occurences of word : ",count)

