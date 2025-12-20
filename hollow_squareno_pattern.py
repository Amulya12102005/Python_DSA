n=5

for rows in range(1,n+1):

    for column in range(1,n+1):
        if rows==1 or rows==n or column==1 or column==n:
            print(column,end=" ")
        else:
            print(" ",end=" ")
    print()