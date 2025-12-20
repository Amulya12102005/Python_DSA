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


    def DeletionAtHead(self, data):
        if self.head==None:
            print("List is empty")
            return
        self.head=self.head.next

    def DeletionAtEnd(self, data):
        if self.head==None:
            print("list is empty")
            return
        if self.head.next==None:
            self.head=None
            return
        temp=self.head
        while temp.next.next!=None:
            temp=temp.next
        temp.next=None

    def display(self):
        if self.head==None:
            print("List is empty")
        temp=self.head
        while temp!=None:
            print(temp.data,end="->")
            temp=temp.next




l1=LinkedList()
l1.InsertionAtHead(10)
l1.InsertionAtHead(20)
#l1.InsertionAtHead(30)
l1.display()
l1.InsertionAtEnd(50)
l1.DeletionAtEnd(10)
l1.display()
