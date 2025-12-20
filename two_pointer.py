arr=[-9,7,9,19,10,6,34]
for i in range(len(arr)):
    for j in range(len(arr)-1-i):
        if arr[j]>arr[j+1]:
            new=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=new
print(arr)
target=16
p1=0
p2=len(arr)-1
while p1<p2:
    sum=arr[p1]+arr[p2]
    if sum<target:
        p1=p1+1
    elif sum==target:
        print(arr[p1],arr[p2])
        p1=p1+1
        p2=p2-1
    else:
        p2=p2-1








