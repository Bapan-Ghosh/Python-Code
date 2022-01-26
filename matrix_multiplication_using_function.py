#matrix multiplication

a=[]
def get_first_matrix(m,n):
    print("Enter the value of First matrix")
    for i in range(m):
        first=[]
        for j in range(n):
            first.append(int(input()))
        a.append(first)
        print()

b=[]
def get_second_matrix(m,n):
    print("Enter the value of First matrix")
    for i in range(m):
        second=[]
        for j in range(n):
            second.append(int(input()))
        b.append(second)    
        print()
    

def print_first_matrix(m,n):
    print("Entered first matrix : ")
    for i in range(m):
        for j in range(n):
            print(a[i][j],end=" ")
        print()

def print_second_matrix(m,n):
    print("Entered second matrix : ")
    for i in range(m):
        for j in range(n):
            print(a[i][j],end=" ")
        print()

res=[[0,0],[0,0]]    
def matrix_mul(m,n):
    for i in range(m):
        for j in range(n):
            res[i][j]=a[i][0]*b[0][j]+a[i][1]*b[1][j] 

def result():
    print("Result after multiplication : ")
    for i in res:
        print(i)
        
m,n=[int(i) for i in input("Enter m*n : ").split()]

get_first_matrix(m,n)
get_second_matrix(m,n)
print_first_matrix(m,n)
print_second_matrix(m,n)
matrix_mul(m,n)
result()
