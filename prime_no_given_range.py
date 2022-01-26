#prime number within a given range
lower=int(input("Enter the starting range :"))
upper=int(input("Enter the end range :"))

if lower>1:
   for i in range(lower,upper+1):
        for j in range(2,i):
          if(i%j==0):
            break
        else:
           print("The prime number is ",i)
else:
    print("Enter a valid no.")           
