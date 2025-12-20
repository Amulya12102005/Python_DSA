arr2D=[
    [1,2,3],
    [4,5,6],
    [7,8,9]]
res = 0
for i in range(len(arr2D)):
    for j in range(len(arr2D[i])):
        if i+j==len(arr2D)-1:
            res = res + arr2D[j][i]
print(res)