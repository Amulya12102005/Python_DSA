arr=[7,3,10,15,-12,13]
window=5
max=arr[0]
sum=0
for i in range(window):
    sum=sum+arr[i]
    if max<sum:
        max=sum
for i in range(window,len(arr)):
    sum=sum+arr[i]
    sum=sum-arr[i-window]
    if max<sum:
        max=sum
print(max)
