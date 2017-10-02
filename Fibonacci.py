cube = lambda x: x**3
def fibonacci(n):
    if n==0: return []
    if n==1: return [0]
    result =[]
    a=0
    b=1
    result=[a,b]
    for i in range(n-2):
        c=a+b
        a,b = b,c
        result.append(c)
    return result

print map(cube, fibonacci(5)) 
