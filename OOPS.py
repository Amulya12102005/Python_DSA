#class Students:
#    name="Amulya"
  #  roll= "24N35A0412"
   # year="3rd Year"

#s1=Students
#print(s1.name)
#print(s1.roll)
#print(s1.year)



class Students:
    def __init__(self,sname,sroll,syear):
        self.name=sname
        self.roll=sroll
        self.year=syear
s1=Students("Amulya",12,"3rd Year")
s2=Students("Bhavana",78,"3rd Year")
s3=Students("Tulsi",13,"3rd Year")
print(s1.name,s1.roll,s1.year)
print(s2.name,s2.roll,s2.year)
print(s3.name,s3.roll,s3.year)