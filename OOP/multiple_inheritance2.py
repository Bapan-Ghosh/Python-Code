#multiple inheritance

class yamaha:
    def __init__(self):
        print("From yamaha")
class honda:
    def __init__(self):
        print("From honda")
class tvs:
    def __init__(self):
        print("From tvs")
class ktm(yamaha,honda,tvs):
    def __init__(self):
        print("From ktm")
        tvs.__init__(self)
        honda.__init__(self)
        yamaha.__init__(self)

obj=ktm()        
