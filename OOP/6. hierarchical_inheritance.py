#hierarchical inheritance
class grand_father:
    print("Grand father")
class baba(grand_father):
    print("baba")
class me(grand_father):
    print("me")

p=me()    
