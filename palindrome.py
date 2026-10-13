list=[]
list.append(input("Enter the first element\n"))
list.append(input("Enter the second element\n"))
list.append(input("Enter the third element\n"))
list.append(input("Enter the fourth element\n"))
list.append(input("Enter the fifth element\n"))
# list.append(input("Enter the sixth element\n"))
print("Your list is",list)
list1=list.copy()
list1.reverse()
if(list==list1):
    print("Your list is a palindrome")
else:
    print("Your list is not palindrome")    