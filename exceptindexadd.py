arr=[5,9,1,2,7]
add_list=[]
add=0
for i in range(0,len(arr)):
    add=add+arr[i]
for i in range(0,len(arr)):
    j=add-arr[i]
    add_list.append(j)
print(add_list)
