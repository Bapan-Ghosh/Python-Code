#string reverse
def reverse(str):
    rev=''
    i=len(str)-1
    while(i>=0):
        rev=rev+str[i]
        i-=1
    return(rev)
str=input("Enter the string ::")
print("Entered string is :",str)
print("The reverse string is :",reverse(str))

"""                   or
   n=input("Enter the string : ")
   for i in range(len(n)):
         l=n[::-1]
   print("Reverse string",l)

 
