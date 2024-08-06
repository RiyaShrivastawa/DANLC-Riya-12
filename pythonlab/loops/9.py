#Q9. Wap to print all the leap years from 1 to n.
n = int(input("enter year"))
year = 1
while year <= n:
    print(f"leap year is 1 to {n}")
    if(year % 4 == 0 and year %100 != 0) or (year % 400 == 0):
        print(year)
    year += 1