x= [[12,7],[7,9],[45,98]]


result = [[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        result[j][i] = x[i][j]
for r in result:
    print(r)