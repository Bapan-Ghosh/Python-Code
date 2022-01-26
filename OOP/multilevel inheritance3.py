class student1:
    def __init__(self,r,n):
        self.roll=r
        self.name=n
class student2:
    def __init__(self,r,n,marks):
        self.marks=marks
        student1.__init__(self,r,n)
    def display(self):
        print(self.roll,self.name,self.marks)

obj=student2(10,'bapan',100)        
obj.display()    
