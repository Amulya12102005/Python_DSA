def binary(arr,k,low,high):
    if low>high:
        return -1

    mid = (low+high)//2
    if arr[mid] == k:
        return mid
    elif arr[mid] < k:
        return binary(arr,k,mid+1,high)
    elif arr[mid] > k:
        return binary(arr,k,low,mid-1)


arr=[-1,0,5,15,20,25,32,40]
k=20
low=0
print(binary(arr,k,low,len(arr)-1))