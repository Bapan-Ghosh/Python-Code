#write a program to create a word from first character of list of words.

n=int(input("Enter the no. of words you want to enter :"))
a=['']*n
s=''
for i in range(n):
    a[i]=input("Enter the word :")
print(a)    
for i in a:
    s=s+i[0]
    print(i)
print("The word is",s)
