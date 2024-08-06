tuples_list = [(1, 2), (3, 4), (5, 6)]
total = sum(sum(tup) for tup in tuples_list)
print("Sum of numbers in tuple :",total)