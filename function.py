def sum(a,b):             #function definition a,b ->parameters
    s=a+b
    return s

print(sum(67,12345678))   #function calling 67,12345678 -> are arguments



def avg(a,b,x):
    s=int((a+b+x)/3)
    return s


print(avg(1234,76,98765))

def calc_prod(a=1,b=1):
    return a*b
print(calc_prod())