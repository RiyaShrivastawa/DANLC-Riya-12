unit = int(input("Enter your unit:"))
bill = 0
if (unit >= 500):
    bill = (unit - 500) * 8 + 100 * 2.5 + 100 * 1.5 + 100 + 1.2
elif (unit >= 400):
    bill = (unit - 400) * 2.5 + 100 * 1.5 + 100 + 1.2

elif (unit >= 300):
    bill = (unit - 300) * 1.5 + 100 * 1.2

elif (unit >= 200):
    bill = (unit - 200) * 1.2

elif (unit <= 200 and unit >= 0):
    bill = 0
else:
    bill = 0
    print("Value shoulg be positive!!")
print("Your bill is:", bill)
