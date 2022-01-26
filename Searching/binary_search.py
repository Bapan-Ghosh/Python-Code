def bsearch(l,val):
    lb=0
    ub=len(l)-1
    while(lb<=ub):
        mid=((lb+ub)//2)
        if(val==l[mid]):
            return mid          #if we want to print value the we have to write l[mid]
        elif(val<l[mid]):
            ub=mid-1
        elif(val>l[mid]):
            lb=mid+1
    return -1        
    
l=[]
n=int(input("Enter the no of elements : "))

def get_data(n):
     for i in range(n):
          l.append(int(input("Enter the number : ")))
          
get_data(n)
l.sort()
print("\n After sorting the numbers are :",l)
val=int(input("Enter the element to search :"))

result=bsearch(l,val)

if(result !=-1):
    print("The number "+str(val)+" present at position",result+1)
    print("The number ",str(val)," present at index",result)
else:
    print("Element is not found")

            
        
            
