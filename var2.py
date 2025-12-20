arr=list(map(int,input().split()))

k=int(input("enter a number"))
flag=False
indx=-1
for i in range(0,len(arr)):
    if arr[i]==k:
        flag=True
        indx=i+2
if flag:
        print(indx)

else:
        print("k not found")


