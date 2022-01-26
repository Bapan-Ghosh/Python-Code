#write a program to remove vowels from a given string
n=input("Enter the string :")

vowel='a' or 'A' ,'e' or 'E', 'i' or 'I', 'o' or 'O' , 'u' or 'U'
for i in n:
    if i in vowel:
        n=n.replace(i,"")
print(n)        
