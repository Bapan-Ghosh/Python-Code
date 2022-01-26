#Addition of two matrix

A=[]
n=int(input("Enter the N * N matrix : for 1st matrix : "))
print("Enter the elements : ")
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input()))    
    A.append(row)
    print()

print(A)

B=[]

n=int(input("Enter the N * N matrix : for 2nd matrix : "))
print("Enter the elements : ")
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input()))
    B.append(row)
    print()
    
print(B)

print("1st matrix in matrix form : ")
for i in range(n):
    for j in range(n):
        print(A[i][j],end=" ")
    print()

print("2nd matrix in matrix form : ")
for i in range(n):
    for j in range(n):
        print(B[i][j],end=" ")
    print()
    
result=[[0,0],[0,0]]

for i in range(len(A)):
    for j in range(len(A)):
         result[i][j]=A[i][j]+B[i][j]

print("Result after addition : ")      
for r in result:
    print(r)

