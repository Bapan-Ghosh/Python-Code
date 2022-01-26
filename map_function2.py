def lower(str):
    print(type(str))
    return str.lower()
    
l=["HeLLO ISHIKA" ,"HOW ARE" ,"YOU !"]
l2=list(map(lower,l))
print("list in lower case :",l2)
print(type(l2))
