def add(x):
    x+=2
    return x

num_list=[10,50,80,2,99]
print("Original list is :",num_list)
num_list=list(map(add,num_list))
print("Modified list is :",num_list)

#map function added 2 of each value of the list
