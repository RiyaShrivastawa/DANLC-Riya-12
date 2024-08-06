dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
concatenated_dict = {k: v for d in (dic1, dic2, dic3) for k, v in d.items()}
print(f"The concatenated dictionary is: {concatenated_dict}")