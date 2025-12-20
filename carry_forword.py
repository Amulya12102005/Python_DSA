arr=[23,24,15,61,7,12,14,96]
carry=[]
max=arr[0]
for i in range(len(arr)):
    if max<arr[i]:
        max=arr[i]
        carry.append(max)
    else:
        carry.append(max)
print(carry)