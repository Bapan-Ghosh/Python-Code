'''The __init__ method is similar to constructors in C++ and Java.
It is run as soon as an object of a class is instantiated. The method is
useful to do any initialization you want to do with your object.'''

class cs_student:
    def __init__(self,roll_no):
        self.roll_no=roll_no

    def set_address(self,address):
        self.address=address

    def print(self):
        print("Roll no : ",self.roll_no)
        print("Address : ",self.address)

r=int(input("Enter the roll no : "))
a=input("Enter the address no : ")
obj=cs_student(r)
obj.set_address(a)
obj.print()
    
        
