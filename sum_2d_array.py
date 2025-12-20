arr2D=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [1,2,3]]

for i in range(len(arr2D)):
    res = 0
    for j in range(len(arr2D[i])):
        res = res+ arr2D[i][j]


    print(res)



