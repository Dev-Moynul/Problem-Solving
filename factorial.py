def fact(x):
    result=1
    if x==1 or x==0:
        print(f'The {x}! is = 1')
    else:
        for i in range(x):
            result=result*(i+1)
        return result
print(fact(5))