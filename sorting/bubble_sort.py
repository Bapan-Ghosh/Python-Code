#Bubble_sort

a=[]
def get_data(n):
    print("Enter the elements : ")
    for i in range(n):
      a.append(int(input()))

def show_data():
    print(a)

def bubble_sort(a,n):
    for i in range(0,n-1):
        for j in range(0,n-i-1,1):
           if(a[j]>a[j+1]):
               temp=a[j]
               a[j]=a[j+1]
               a[j+1]=temp
    
n=int(input("Enter the no. of elements : "))
get_data(n)
print("Entered elements : ")
show_data()
bubble_sort(a,n)
print("Elements after sorting : ")

show_data()
