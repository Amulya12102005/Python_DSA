arr2D=[
    [1,2,3],
    [4,5,6],
    [7,8,9]]
res = 0
for i in range(len(arr2D)):

            res = res + arr2D[i][i]
print(res)