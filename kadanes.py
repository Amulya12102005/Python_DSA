arr=[-5,-3,-2,-1,0,1,2,3]
maxi=arr[0]
current=0
for i in range (len(arr)):
    current+=arr[i]
    if maxi<current:
        maxi=current
    if current<0:
        current=0
print(maxi)