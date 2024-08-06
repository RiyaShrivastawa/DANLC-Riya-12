#2. Write a Python program to Return a set of elements present in Set A or B, but
#not both.
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
new_set = set1.symmetric_difference(set2)
print("element in set 1 and 2 but not in both are :",new_set)