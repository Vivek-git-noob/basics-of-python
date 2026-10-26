class Student:
    college="Bit mesra"  #class attributes same for every object
    def __init__(self,name,roll,marks,hobby):  #this is a constructor
        self.name=name
        self.roll=roll
        self.marks=marks
        self.hobby=hobby

    def greetings(self):
        print("GOOOOOD MORNING",self.name)
        
    def get_marks(self):
        print("The marks of",self.name,"is",self.marks)    

s1=Student("Vivek kumar",40,69,"Watching films")
s2=Student("Shivani",41,99,"Badminton")
s3=Student("Tony",42,100,"Making robots")  
# print(s2.roll)    
# print(s1.college) 
# print(s3.college) 
s1.greetings()
s2.greetings()
s3.greetings()
s1.get_marks()
s2.get_marks()
s3.get_marks()