#multilevel inheritance

class Grandfather:
    def __init__(self,g):
        self.grandfather=g
        
class father(Grandfather):
    def __init__(self,f,g):
        self.fathername=f
        Grandfather.__init__(self,g)
        
class son(father):
    def __init__(self,s,f,g):
        self.sonname=s
        father.__init__(self,f,g)
    def print_name(self):
        print("son name :",self.sonname)
        print("fathername :",self.fathername)
        print("grandfather name :",self.grandfather)

p1=son('bapan','nirmal','kalipada')
p1.print_name()

