n=(int(input("Enter the no. ")))
flag=0
if(n>1):
    
   for i in range(2,n):
        if(n%i==0):
           flag=1
           break
    
   if(n==1):
       print(n," neither prime nor no prime ")
   elif(flag==0):
       print("Given no. ",str(n)," is prime ")
   else:
       print("Given no. is not prime ")
else:
    print("Enter a valid input")
                                             
