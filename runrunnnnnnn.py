class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def study(self):
        print(self.name,"is studying")
#Creating Objects
s1=Student("Ram",20)
s2=Student("Rahul",20)
#Accessing Methods
s1.study()
s2.study()




