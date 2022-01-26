#binary_search

a=[]
def get_data(n):
    print("Enter the elements : ")
    for i in range(n):
        a.append(int(input()))
        
def printt():
    print("Entered elements : ")
    print(a)
    
def b_search(key,a,n):
    lb=0
    ub=n-1
    while(lb<=ub):
        mid=((lb+ub)//2)
        if(a[mid]==key):
            return mid
        elif(key>a[mid]):
            lb=mid+1
        else:
            ub=mid-1
    return -1        

n=int(input("Enter the no. of elements : "))
get_data(n)
printt()

a.sort()
print("List after sorted order because binary only applicable on sorted order list : \n",a)
key=int(input("Enter the element to search whether it is present in the list or not : "))

res= b_search(key,a,n)

if(res==-1):
    print(key,"is not present in the list : ")
else:
    print(key,"is present at position ",res+1)
