'''series of no.'''
n=int(input("Enter the no. of series"))
sum=0
for i in range(0,n-1,1): #range(5,0,-1) means start from 5 and end at 1
    sum=sum+n%10
    n=n//10
print(sum)    
    

      #for loop : range(start,end,increment)
