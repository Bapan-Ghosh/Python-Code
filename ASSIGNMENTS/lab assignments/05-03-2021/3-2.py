s=input("enter your name:")
c=0
pos=0
for i in s:
    if(i==' '):
        c=c+1
print(s[0]+'.',end='')
for i in s:
    pos=pos+1
    if(i==' ' and c==1):
        break     
for i in range(pos,len(s)):
    print(s[i],end='')
