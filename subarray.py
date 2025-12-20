arr=[1,2,3,4]
for i in range(len(arr)):
    for j in range(i,len(arr)):                                    #basic subarray
        for k in range(i,j+1):
            print(arr[k],end="")
        print()



arr=[10,-2,-3,4,5]
k=3
max=arr[0]
for i in range(len(arr)):
    count=0
    for j in range(i,len(arr)):
        count=count+arr[j]                                                 #for maximum element in an array
        if max<count and count<=k:
            max=count
print(max)




arr=[1,2,3,4]
res=0
for i in range (len(arr)):
    for j in range (i,len(arr)):                                                     #sum of all the sub array
        for k in range(i,j+1):

            res=res+arr[k]
print(res)