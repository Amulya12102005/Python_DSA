arr=[1,0,1,1,0,1,1,1,0,1,0,0,1,1]
max_count=0
current_count=0
for i in range(0,len(arr)):
    if arr[i]==1:
        max_count=max_count+1
        if current_count<max_count:
            current_count=max_count
    else:
        max_count=0
print(current_count)






