n=int(input("Enter the number :"))
rev=0
while(n!=0):
    rev=rev*10+n%10
    n=n//10           #float division
print("rev :",rev)
