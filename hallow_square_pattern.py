n=5
num = "*"
for rows in range(1,n+1):

    for column in range(1,n+1):
        if rows==1 or rows==n or column==1 or column==n or rows+column==n+1 or rows==column:
            print(num,end=" ")
        else:
            print(" ",end=" ")
    print()