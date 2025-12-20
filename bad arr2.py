arr=[1,1,11,12,15,16]
flag=True
index=-1

for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):

        if arr[i]==arr[j]:
            flag = False
            index=i
if flag:
    print("it ia a good array")
else:
    print("it is a bad array")
