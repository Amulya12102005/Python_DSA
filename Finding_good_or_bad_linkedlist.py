class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def InsertionAtHead(self, data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def InsertionAtEnd(self, data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node



    def display(self):
        temp=self.head

        while temp!=None:
            print(temp.data,end="->")
            temp=temp.next

    def duplicate(self):
        unique=set()
        temp=self.head
        flag=True
        while temp:
            if temp.data in unique:
                flag=False
                print("bad list")
                return
            else:
                unique.add(temp.data)
            temp=temp.next
        if flag:
            print("Good list")


l1=LinkedList()
l1.InsertionAtHead(10)
l1.InsertionAtHead(20)

#l1.display()

l1.InsertionAtEnd(50)
l1.display()
l1.duplicate()
l1.display()



