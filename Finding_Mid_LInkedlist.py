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


    def Mid(self):
        slow=self.head
        fast=self.head
        while fast.next!=None and fast.next.next!=None:

            slow = slow.next
            fast=fast.next.next

        print(slow.data)



    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end="->")
            temp=temp.next
l1=LinkedList()
l1.InsertionAtHead(10)
l1.InsertionAtHead(20)
l1.InsertionAtHead(30)
#l1.InsertionAtHead(40)
#l1.display()


l1.display()
print()
l1.Mid()
