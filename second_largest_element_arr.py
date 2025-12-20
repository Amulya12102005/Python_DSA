arr=[1,95,45,85,63,74]
if arr[0]>arr[1]:
    first=arr[0]
    last=arr[1]
else:
    first=arr[1]
    last=arr[0]
for i in range(2,len(arr)):
    if first<arr[i]:
        last=first
        first=arr[i]
    elif arr[i]>last and arr[i]!=first:
        last=arr[i]

print(last)