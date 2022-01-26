#factorial
n=int(input("Enter the value to find factorial :"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("Factorial of given ",n ," is",fact)
