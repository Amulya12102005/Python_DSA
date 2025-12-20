arr=[-15,-20,-1,-3]
max=arr[0]
for i in range (len(arr)):
    for j in range (i,len(arr)):
        count=0                                                           #for maximum subarray
        for k in range(i,j+1):
            count=count+arr[k]
        if max<count:
            max=count
print(max)


arr=[-15,-20,-1,-3]
min=arr[0]
for i in range (len(arr)):                                                #for minimum subarray
    for j in range (i,len(arr)):
        count=0
        for k in range(i,j+1):
            count=count+arr[k]
        if min>count:
            min=count
print(min)



arr=[-15,-20,-1,-3]
max=arr[0]
for i in range (len(arr)):
    count=0
    for j in range (i,len(arr)):
        count=count+arr[j]                                                  #to reduce the time complexity I have removed one for loop
        if max<count:
            max=count
print(max)




