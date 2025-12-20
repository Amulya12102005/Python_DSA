arr=list(map(int,input().split()))

k=int(input("enter a number"))
for i in range(0,len(arr)):
    if arr[i]==k:
        print(i)
        break
else:
        print("k not found",i)