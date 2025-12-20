def prefix_sum(prefix,left,right):
    if left==0:
        return prefix[right]
    else:
        return prefix[right]-prefix[left-1]
arr = [10, 20, 30, 40, 50]
prefix=[]
prefix.append(arr[0])
for i in range(1,len(arr)):
    prefix.append(prefix[i-1]+arr[i])
print(prefix_sum(prefix,left=0,right=3))
print(prefix_sum(prefix,left=1,right=4))
print(prefix_sum(prefix,left=2,right=3))