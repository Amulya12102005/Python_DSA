arr=[12,14,19,4,6,0,-1]
for i in range(1,len(arr)):
    currentVal=arr[i]
    j=i-1
    while j>=0 and arr[j]>currentVal:
        arr[j+1]=arr[j]
        j-=1
        arr[j+1]=currentVal
print(arr)