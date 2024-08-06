def count_and_display_vowels(text):
    vowels = "aeiouAEIOU"
    vowel_counts = {vowel: 0 for vowel in vowels}

    for char in text:
        if char in vowel_counts:
            vowel_counts[char] += 1

    total_vowels = sum(vowel_counts.values())

    for vowel, count in vowel_counts.items():
        print(f"'{vowel}': {count}")

    print(f"\nTotal number of vowels: {total_vowels}")

str1 = input("Enter the string:")
count_and_display_vowels(str1)