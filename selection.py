arr=[21,42,44,49,23,0,-1,17]

for i in range(len(arr)-1):
    mini=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[mini]:
            mini=j
    new=arr[mini]
    arr[mini]=arr[i]
    arr[i]=new
for a in range(len(arr)):
    print(arr[a],end=" ")

