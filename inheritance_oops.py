class Box:
    def __init__(self):
        print("box")
    def Box1(self):
        print("Box1")
    def Box2(self):
        print("Box2")

class Minibox(Box):

        def Minibox1(self):
            print("Minibox1")
        def Minibox2(self):
            print("Minibox2")

m1=Minibox()
m1.Minibox1()
m1.Box1()


