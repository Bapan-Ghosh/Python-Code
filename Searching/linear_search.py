#Linear search

l=[]
def get_data(n):
    print("Enter the elements :")
    for i in range(n):
        l.append(int(input()))
def printt(n):
    print(l)

def linear_search(key,n,l):
    for i in range(n):
        if(key==l[i]):
            return i
    return -1       
        
n=int(input("Enter the number of elements : "))
get_data(n)
printt(n)

key=int(input("Enter the key to search : "))
res=linear_search(key,n,l)

if(res==-1):
    print(key,"is not present in the list : ")
else:
    print("element is present at index",res)
