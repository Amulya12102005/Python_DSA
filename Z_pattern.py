n=5
num="*"
for i in range(n):
    for j in range (n):
        if i==0 or i==n-1 or j==n-i-1 :
            print(num,end=" ")
        else:
            print(" ",end=" ")
    print()