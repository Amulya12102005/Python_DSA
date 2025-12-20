def even(element):
    return element%2==0
arr=[-1,0,17,21,42,44,49,50,52,23]
new_arr=list(filter(even,arr))
print(new_arr)