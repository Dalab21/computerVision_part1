def apply_func(func, x,y):
    return func(x,y)

def add(x,y):
    return x+y

def multiply(x,y):
    return x*y

#result = apply_func(add,3,4)
#print(result)


def operations(sum, x,y):
    return sum(x,y)
    

def addtion(a,b):
    sum=a+b
    return sum

print(operations(addtion,12,4)) # sum(x,y)


