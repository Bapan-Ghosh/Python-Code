#Quick_sort

a=[]
def get_data(n):
    print("Enter the elements : ")
    for i in range(n):
      a.append(int(input()))

def show_data():
    print(a)

def swap(a,i,j):
    temp=a[i]
    a[i]=a[j]
    a[j]=temp

def partition(a,l,r):
    pivot=a[r]
    j=l
    i=l-1
    while(j<r):
        if(a[j]>pivot):
            i+=1
            swap(a,i,j)
        j=j+1
    swap(a,i+1,r)
    return(i+1)        

def Quick_sort(a,l,r):
    if(l<r):
        pi=partition(a,l,r)

        Quick_sort(a,l,pi-1)
        Quick_sort(a,pi+1,r)
    
        
n=int(input("Enter the no. of elements : "))
get_data(n)
print("Entered elements : ")

show_data()

Quick_sort(a,0,n-1)

print("Elements after sorting : ")

show_data()
