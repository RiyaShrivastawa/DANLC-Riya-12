str1 = input("Enter a string:")
str = str1.split()
str2 = " "
for word in str:
    str2 += word[::-1]+" "
print(str2)