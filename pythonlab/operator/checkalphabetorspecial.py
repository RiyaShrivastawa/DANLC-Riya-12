#check alphabet or special
ch = input("Enter your character:")
if(ch>= 'a' and ch<='z') or (ch>='A' and ch<='Z'):
    print("It is an alphabet")
elif(ch>='0' and ch<='9'):
    print("It is digit")
else:
    print("It is special character")
