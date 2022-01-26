#insertion_sort

a=[]
def get_data(n):
    print("Enter the elements : ")
    for i in range(n):
      a.append(int(input()))

def show_data():
    print(a)

def insertion_sort(a,n):
    for i in range(1,n):
        current=a[i]
        j=i-1
        while(a[j]>current and j>=0):
            a[j+1]=a[j]
            j=j-1
        a[j+1]=current
        
n=int(input("Enter the no. of elements : "))
get_data(n)
print("Entered elements : ")
show_data()
insertion_sort(a,n)
print("Elements after sorting : ")

show_data()
