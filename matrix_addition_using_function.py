#matrix addition
a=[]
def fist_matrix(m,n):
    print("Enter the value of first matrix :")
    for i in range(m):
        f=[]
        for j in range(n):
           f.append(int(input()))
        a.append(f)
        print()

b=[]    
def second_matrix(m,n):
    print("Enter the value of second matrix :")
    for i in range(m):
        s=[]
        for j in range(n):
           s.append(int(input()))
        b.append(s)
        print()
c=[[0,0],[0,0]]        
def matrix_addition(m,n):
    for i in range(m):
        for j in range(n):
            c[i][j]=a[i][j]+b[i][j]
            print(end=" ")
    print()

def result(m,n):
    print("Result :")
    for i in c:    
        print(i)      
m,n=[int(i) for i in input("Enter the m*n").split()]
fist_matrix(m,n)
second_matrix(m,n)

print("Entered first matrix :")
for i in range(m):
    for j in range(n):
        print(a[i][j],end=" ")
    print()    

print("Entered second matrix :")
for i in range(m):
    for j in range(n):
        print(b[i][j],end=" ")
    print()
    
matrix_addition(m,n)

result(m,n)

