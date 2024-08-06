#Wap to read age of 15 people and find the number of adults, babies and school age students.
adult_num = 0
babies_num = 0
school_age_num = 0
count = 0
print("Enter the age of 15 people :")
while count < 15:
    age = int(input())
    count += 1
    if age < 3:
        babies_num += 1
    elif age < 18:
        school_age_num += 1
    else:
        adult_num += 1
print("no of adult people", adult_num)
print("no of school age people", school_age_num)
print("no of babies people", babies_num)

