arr=[-1,0,17,21,23,42,44,49]
k=44
low=0
high=len(arr)-1

while low<=high:
    sumhl=high+low
    mid=sumhl//2
    if arr[mid]==k:
        print("target found at index",mid)
        break
    elif arr[mid]<k:
        low=mid+1
    else:
        high=mid-1
