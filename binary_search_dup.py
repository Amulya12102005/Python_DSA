arr=[-1,0,17,21,23,42,42,42,42,44,49]
k=42
low=0
high=len(arr)-1
indx=-1
while low<=high:                                            #first and last occurance
    sumhl=high+low
    mid=sumhl//2
    if arr[mid]==k:
        indx=mid
        low=mid+1         #high=mid-1
    elif arr[mid]<k:
        low=mid+1
    else:
        high=mid-1
print(indx)