def NoOfCoprimes(num_list,length):
    count = 0
    for i in range(0, length-1) : 
        for j in range(i+1, length) : 
      
            if (Coprime(num_list[i], num_list[j])) : 
                count = count + 1
    return count
def Coprime(a,b):
     return (gcd(a, b) == 1)
def gcd(a,b):
      
    if (a == 0 or b == 0): 
            False
    if (a == b): 
        return a 
  
    if (a > b): 
        return gcd(a-b, b) 
          
    return gcd(a, b-a)

test_case=int(input())
for i in range(0,test_case):
    num=int(input())
    num_list=[]
    for i in range(1,num+1):
        if(num%i==0):
            num_list.append(i)
    length=len(num_list)
    print(num_list)
    print(NoOfCoprimes(num_list,length))
