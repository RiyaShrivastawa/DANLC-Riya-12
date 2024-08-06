def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in input_string:
        if char in vowels:
            vowel_count += 1
    return vowel_count
input_string = input("Enter your string:")
total_vowels = count_vowels(input_string)
print(f"Input: {input_string}")
print(f"Total vowels are: {total_vowels}")