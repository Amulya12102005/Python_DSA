arr=[12,-9,14,45,76,15,33,-9]

for i in range(len(arr)):
    for j in range(len(arr)-1-i):
        if arr[j]>arr[j+1]:
            new=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=new
print(arr)
flag=False
#indx=-1
for i in range(len(arr)-1):
    if arr[i]==arr[i+1]:
        flag=True
        #indx=i
if flag:
    print("it is  a bad array")
else:
    print("it is  a good array")


