'''A
   AB
   ABC
   ABCD
   ABCDEF'''

n=int(input("Enter the no. of row :"))

for i in range(1,n+1):
    ch='A'
    for j in range(1,i+1):
        print(ch,end="")
        ch=chr(ord(ch)+1)  #CH=B(97+1)
    print()    







