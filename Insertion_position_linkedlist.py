class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def InsertionAtPosition(self,data,pos):
        new_node=Node(data)
        if pos < 1:
            print("Invalid position")
            return
        if head ==None:
            print("List is empty")
            return

        if pos == 1:
            self.head = self.head.next
            return
        temp = self.head
        count=1
        while temp.next!= None and count<pos-1:
            temp.next = temp.next.next
            count = count + 1
        if temp.next == None:
            print("List is empty")
        temp.next = temp.next.next
        #if temp==None:
         #   print("Invalid range")
          #  return
        #new_node.next=temp.next
        #temp.next = new_node

    def display(self):
        temp=self.head
        while temp!= None:
            print(temp.data,end=" ")
            temp = temp.next

l1=LinkedList()
l1.InsertionAtPosition(10,10)
l1.InsertionAtPosition(10,10)
l1.InsertionAtPosition(10,10)
l1.display()




















