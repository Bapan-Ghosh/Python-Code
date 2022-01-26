#introduction 2

class Myclass:
    def __init__(self,x):       #it's a constructor
           self.x=x+5

n=int(input("Enter the value "))  
obj=Myclass(n)

print(obj.x)
