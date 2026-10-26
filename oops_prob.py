# sub1=input("Enter the subject1 name\n")
# sub2=input("Enter the subject2 name\n")
# sub3=input("Enter the subject3 name\n")
# marks1=input("Enter the marks of",sub1,"\n")
# marks2=input("Enter the marks of",sub2,"\n")
# marks3=input("Enter the marks of",sub3,"\n")
class Student:
    def __init__(self,sub1,sub2,sub3,marks1,marks2,marks3):
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
        

    def avg(self):
     print("The marks are",self.marks1,self.marks2,self.marks3)
     print("Their average is",(self.marks1+self.marks2+self.marks3)/3)


s1=Student("DBMS","OOPS","CN",67,54,99)
s1.avg()
 