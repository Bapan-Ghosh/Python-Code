#selection sort

def selection_sort(a,n):
    for i in range(n-1):
        for j in range(i+1,n,1):
            if(a[i]>a[j]):
                temp=a[i]
                a[i]=a[j]
                a[j]=temp           
    return a

a=[]

def get_data(n):
    for i in range(n):
        a.append(int(input("Enter the no. : ")))

n=int(input("Enter the no. of elements : "))

get_data(n)

res=selection_sort(a,n)

print("Elements after sorting :",res)
