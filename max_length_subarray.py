arr=[-2,-1,0,1,2]
max_length=0
k=3
for i in range(len(arr)):
    sum=0
    for j in range(i,len(arr)):
        sum+=arr[j]
        if sum<=k:
            if max_length<j-i+1:
                max_length=j-i+1
print(max_length)