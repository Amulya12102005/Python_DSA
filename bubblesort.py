arr=[12,-9,14,45,76,15,33]
flag=False
indx=-1

for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            sorted([arr[i],arr[j]])
            flag=True
            indx=i
if flag:
    print(sorted(arr))

