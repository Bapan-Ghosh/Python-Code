#multilevel
class TATA_MOTORS:
    def __init__(self):
        print("From tata motors :")
    def display(self):
        print("******")
class BMW(TATA_MOTORS):           #If we don't write (TATA MOTORS) here, then print(***) will not be execute and we will get an error     
    def __init__(self):
        print("From BMW :")
        TATA_MOTORS.__init__(self)
class jaguar(BMW):
    def __init__(self):
        print("From jaguar :")
        BMW.__init__(self)
class land_rover(jaguar):
    def __init__(self):
        print("From land rover")
        jaguar.__init__(self)
class Audi(land_rover):
    def __init__(self):
        print("From audi")
        land_rover.__init__(self)

obj=Audi()
obj.display()
