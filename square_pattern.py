n=4
num = "*"
for rows in range(n):

    for column in range(n):
        if rows==0 or rows==n-1 or column==0 or column==n-1:
            print(num,end=" ")
        else:
            print(" ",end=" ")
    print()





