#check correct currency
currency = int(input("Enter your currency value:"))
if(currency == 2000 or currency== 500 or currency == 200 or currency == 100 or currency == 50):
    print("Correct currency")
else:
    print("not correct currency")