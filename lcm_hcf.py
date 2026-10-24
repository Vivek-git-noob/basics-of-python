num1=int((input("Enter the fisrt desired number\n")))
num2=int((input("Enter the second desired number\n")))
def hcf_lcm(num1,num2):
    product=num1*num2
    while(num2!=0):
        rem=num1%num2
        num1=num2
        num2=rem
    hcf=num1
    lcm=(product/hcf)
    return lcm,hcf
print(hcf_lcm(num1,num2))