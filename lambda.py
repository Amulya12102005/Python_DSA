arr=[-1,0,17,21,42,44,49,50,52,23]
new_arr=list(map(lambda element:element%2==0,arr))                           #by using map will be getting the boolean values and by filter :
print(new_arr)                                                                #list(filter(lambda element:element%2==0,arr))