def safe_list_access(lst, index):
    try:
        return lst[index]
    except IndexError:
        return f"Error: Index {index} is out of range. The list has {len(lst)} elements."
    except Exception as e:
        return f"Unexpected error: {e}"

lists = [ [1, 2, 3, 4, 5],[],['a', 'b', 'c'] ]

indices = [2,-1, 10, 'a']

for lst in lists:
    for index in indices:
        result = safe_list_access(lst, index)
        print(f"List: {lst}, Index: {index} -> {result}")