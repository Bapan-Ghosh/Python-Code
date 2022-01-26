a=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    a.append(int(input("Enter element:")))
    #a.append(b)
num=int(input("Enter the number to check :"))
for i in range(n):
    if(num==a[i]):
      print("The number "+ str(num) +" present at location",i)
