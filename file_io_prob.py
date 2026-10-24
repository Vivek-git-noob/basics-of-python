# f=open("practice.txt","a+")
# f.write("Hi everyone\nwe are learning File I/O\nusing java\nI like programming in java")
# f.close()
f=open("practice.txt","r")
data=f.read()
new_data=data.replace("java","python")
print(new_data)
f.close()
f=open("practice.txt","w")
f.write(new_data)

def check_word():
    f=open("practice.txt","r")
    n_data=f.read()
    if(n_data.find("learning")!=-1):
        print("exists")
    else:
        print("it does not exist")
f.close()



check_word()
























