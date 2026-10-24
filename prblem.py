def sum_num(n):
    if (n==1):
        return 1
    return n+sum_num(n-1)

print(sum_num(20))

n=int(input("Enter the desired number\n"))
sum=0
while(n>0):
    sum=sum+n
    n-=1
print(sum)
print()

def print_list(list,idx=0):
    if (idx==len(list)):
         return
    else:
     print((list[idx]))
     print_list(list,idx+1)  

marks=[67.66,45.5,66,90,34]
print_list(marks)   

    