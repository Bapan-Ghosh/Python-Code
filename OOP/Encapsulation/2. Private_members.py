#Private members
class Base:
    def __init__(self):
        self.a="Bapan ghosh"
        self.__c="Bapan ghosh"

class Derived(Base):
    def _init_(self):
        Base.__init__(self)
        print("Calling private member of base class :")
        print(self.__c) # This will give you an error

obj=Derived(self)
print(obj.a)
print(obj.__c)
