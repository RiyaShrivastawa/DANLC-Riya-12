#Q8. Wap to input 10 numbers from user and find the minimum and maximum number.

numbers = []
print("enter your number:")
for _ in range(10):
    number = int(input())
    numbers.append(number)
min_number = min(numbers)   #find min number
max_number = max(numbers)  #find min number
print("minimum number is :", min_number)
print("maximum number is :", max_number)
