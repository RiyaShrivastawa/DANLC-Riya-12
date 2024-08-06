def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit) ** num_digits
    return sum == num

def find_armstrong_numbers(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        if is_armstrong(num):
            armstrong_numbers.append(num)

    return armstrong_numbers



start_range = 100
end_range = 1000

print(f"Armstrong numbers between {start_range} and {end_range}:")
print(find_armstrong_numbers(start_range, end_range))