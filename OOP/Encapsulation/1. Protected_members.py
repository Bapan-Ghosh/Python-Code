#Protected members

class Base:
    def __init__(self):
        self._a=2  #procted member
        #print(self._a)

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("calling protected member of base class : ")
        print(self._a)

obj1=Derived()

obj2=Base()
print(obj2.a)

'''This will give us an error because protected member can be
                 acces within the class and its subclasses'''
