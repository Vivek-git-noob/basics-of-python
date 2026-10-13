num1=int(input("Enter the desired 1st number\n"))
num2=int(input("Enter the desired 2nd number\n"))
num3=int(input("Enter the desired 3rd number\n"))
print("Your three numbers are",num1,num2,num3)
if(num1>=num2 & num1>=num3):
    print(num1,"is the greatest number")
elif(num2>=num3):
    print(num2,"is the greatest number") 
else:
    print(num3,"is the greatest number")      