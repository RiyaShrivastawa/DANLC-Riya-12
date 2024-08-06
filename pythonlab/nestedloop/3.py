print("Enter start and end range for table")
start = int(input())
end = int(input())
for i in range(1,11):
    for n in range(start , end+1):
        print(n*i , "\t" , end="")
    print()
