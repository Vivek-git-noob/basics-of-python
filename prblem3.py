list1=[1,4,9,16,25,36,49,64,81,100]
num=int(input("ENTER THE NUMBER YOU WANT TO SEARCH\n"))
for el in list1:

    if(el==num)  :
        print("found")
        break
else:
     print("not found")  

