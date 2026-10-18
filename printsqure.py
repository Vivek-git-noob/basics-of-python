n=1
list1=[]
while n<11:
    list1.append(n*n)
    n+=1

print(list1)




num=int(input("Enter the number you want to search\n"))

p=0
found=False
while p<len(list1):
    if(list1[p]==num):
        found=True
        break
    p+=1
if(found):
    print(num,"found in the list")
else:
    print(num,"was not found in the list")

 
