#check login password
userid = "ashita@gmail.com"
password = "ash@123"
uid = input("Enter your userid")
if(uid == userid):
     pass1 = input("Enter your password")
     if(pass1 == password ):
         print("valid password")
     else:
         print("Invalid password")
else:
  print("invalid userid")