#gcd
a=int(input("Enter the first no. :"))
b=int(input("Enter the second no. :"))

while a != b:  
 if(a == b):
    print("gcd no. is:",a)
 elif a > b:
    a=a-b
 else:
    b=b-a
print(a)
