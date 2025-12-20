arr=[10,-2,-3,5]
k=-1
min=arr[0]
for i in range(1,len(arr)):
    if min>arr[i]:
        min=arr[i]
max=min
for i in range(len(arr)):
    count=0
    for j in range(i,len(arr)):
        count=count+arr[j]
        if max<count and count<=k:
            max=count
print(max)