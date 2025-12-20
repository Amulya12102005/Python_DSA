def binary (arr,k):
    low = 0
    high = len(arr) - 1
    while low <= high:
        sumhl = high + low
        mid = sumhl // 2
        if arr[mid] == k:
            print("target found at index", mid)
            break
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1


binary([-1,0,5,15,20,25,32,40],25)