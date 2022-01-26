#multilevel inheritance

class person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def display(self):
        print("Name :",self.name)
        print("age :",self.age)
class person1(person):
    def __init__(self,n,a,add):
        person.__init__(self,n,a)
        self.address=add
    def displayadd(self):
        print("Address :",self.address)

class person2(person1):
    def __init__(self,n,a,add,m):
        person1.__init__(self,n,a,add)
        self.mobile=m
    def displaymobile(self):
        print("Mobile :",self.mobile)


p1=person2("bapan",25,"kolkata",999)
p1.display()
p1.displayadd()
p1.displaymobile()
