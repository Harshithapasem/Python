arr=[5,9,1,2,7]
product_list=[]
product=1
for i in range(0,len(arr)):
    product=product*arr[i]
for i in range(0,len(arr)):
    j=product/arr[i]
    product_list.append(j)
print(product_list)
