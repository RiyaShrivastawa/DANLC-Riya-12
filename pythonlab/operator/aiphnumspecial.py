ch = ord(input("Enter your character:"))
if(ch)>= 65 and (ch)<=90 or (ch) >= 97 and (ch) <= 122 :
    print("It is an alphabet")
elif(ch)>= 48 and (ch)<= 57:
    print("It is a number!")
else:
    print("It is an special character!")