#multiple_inheritance

class Base1:
    def __init__(self):
        self.str1=" Geek 1"
        print("Base 1")
class Base2:
    def __init__(self):
        self.str2="Geek 2"
        print("Base2")
class Derived(Base1,Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")
    def print(self):
        print(self.str1,"\n",self.str2)

ob=Derived()
ob.print()
        
