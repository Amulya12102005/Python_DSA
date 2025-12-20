n=4
num = 1
for rows in range(n,0,-1):

    for column in range(1,rows+1):
        print(num,end=" ")
        num += 1

    print()