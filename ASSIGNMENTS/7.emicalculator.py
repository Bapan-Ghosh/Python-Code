p=float(input("Enter the principal :"))
r=float(input("Enter the rate of interest :"))
n=float(input("Enter the loan term in months :"))
r=(r/12)/100
print(r)
E=p*r*(((1+r)**n)/(((1+r)**n)-1))
print("The EMI is",E)
