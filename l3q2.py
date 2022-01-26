p=int(input("Enter the value of p: "))
q=int(input("Enter the value of q: "))

start=int(input("Enter start range:"))
end=int(input("Enter end range:"))
print("_______________________________________________")
print("numbers divisible only by ",p,"and not by ",q,"are:")
for i in range(start,end+1):
    if(i%p==0 and i%q!=0):
        print(i,end=" ")
