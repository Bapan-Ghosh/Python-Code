#Multiplication of two matrix

m,n=(int(p) for p in input("Enter the (Row * Column)m*n matrix : ").split())

A=[]
print("Enter the 1st matrix elements : ")
for i in range(m):
    row=[]
    for j in range(m):
        row.append(int(input()))
    A.append(row)
    print()


B=[]
print("Enter the 2nd matrix elements : ")
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input()))
    B.append(row)
    print()

print("First list in matrix form :")

for i in range(m):
    for j in range(n):
        print(A[i][j],end=" ")
    print()    
        
print("Second list in matrix form :")

for i in range(m):
    for j in range(n):
        print(B[i][j],end=" ")
    print()

mul=[[0,0],[0,0]]
ml=[]
for i in range(len(A)):
    for j in range(len(B)):
        mul[i][j]=0
        for k in range(len(B)):
            mul[i][j]=mul[i][j]+A[i][k]*B[k][j]
        ml=mul    

print("Result after multiplication : ")
for r in ml:
    print(r)
