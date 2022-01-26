#armstrong number
n=int(input("Enter the number : "))
s=0
temp=n
while(temp!=0):
    r=temp%10
    s=s+(r**3)
    temp=temp//10

if(s==n):
    print("Given number is an armstrong number :")
else:
    print("Given number is not an armstrong number :")


