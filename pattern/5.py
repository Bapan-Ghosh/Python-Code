n=int(input("Enter the value of n"))
for i in range(1,n+1,1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end="")
    print()      #this function for next line(\n)    
