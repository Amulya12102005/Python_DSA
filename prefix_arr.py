def prefix(arr,left,right):
    pre_arr = []
    prefix_sum = 0
    for i in arr:
        prefix_sum = prefix_sum + i
        pre_arr.append(prefix_sum)
    return pre_arr

arr = [23, 24, 10, 61,7,12,14,96]
print(prefix(arr,0,3))
print(prefix(arr,1,4))
print(prefix(arr,2,3))

count=0
for i in range(left)

left = int(input())
right = int(input())

if left == 0:
    print(pre_arr[right])
else:
    print(pre_arr[right] - pre_arr[left - 1])


