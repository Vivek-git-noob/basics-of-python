cities=["mum","del","har","kol","rnc","goa"]
def length(list):
    return len(list)
def elements(list):
    for el in list:
        print(el,end=" ")
    

print(length(cities))
elements(cities)
print()


num=int(input("Enter the the desired number\n"))
def fact(num):
    factorial=1
    i=1
    while i<=num:
        factorial=factorial*i
        i+=1
    return factorial

print("The factorial of",num,"is",fact(num))    

usd=float(input("Enter the desired amount in usd\n"))
def converter(usd):
    rupee=usd*100
    return rupee
print(usd,"dollars in Indian rupee is",converter(usd),"rupees")


num2=int(input("Enter the desired number\n"))
def odd_even(num2):
    if num2%2==0:
        return "even"
    else:
        return "odd"

print(odd_even(num2))    