def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
count = 0
num = 2

print("The first 10 prime numbers are:")

while count < 10:
    if is_prime(num):
        print(num)
        count += 1
    num += 1