arr2D=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [1,2,3]]
print(len(arr2D))
for i in range(len(arr2D)):
    for j in range(len(arr2D[i])):
        print(arr2D[i][j],end=' ')
    print()