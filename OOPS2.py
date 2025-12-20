class Students:
    def __init__(self,sname,sroll,syear):
        self.name=sname                                                        #constructor
        self.roll=sroll
        self.year=syear

    def aboutstudent(self):
        print(self.name,self.roll,self.year)                                      #method it should be inside the class
s1=Students("Amulya",12,"3rd Year")
s2=Students("Bhavana",78,"3rd Year")
s3=Students("Tulsi",13,"3rd Year")
s1.aboutstudent()
s2.aboutstudent()
s3.aboutstudent()





class Pen:
    def __init__(self,pbrand,pcolor,ptype,pprice):
        self.brand=pbrand
        self.color=pcolor
        self.type=ptype
        self.price=pprice
    def aboutpen(self):
        print(self.brand,self.color,self.type,self.price)
p1=Pen("cello","blue","gel",20)
p2=Pen("bitco","black","ballpointer",15)
p1.aboutpen()
p2.aboutpen()

