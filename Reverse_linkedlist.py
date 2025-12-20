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
        sum=0
        count=0
        while temp!=None:
            print(temp.data,end="->")
            sum=sum+temp.data
            count=count+1
            temp=temp.next

        print(sum)
        print(count)
        def reverse(self):
            temp=self.head
            st=[]
            while temp!=None:
                st.append(temp.data)
                temp=temp.next
            while st:
                print(st[-1],end="->")
                st.pop()
l1=LinkedList()
l1.InsertionAtHead(10)
l1.InsertionAtHead(20)
l1.InsertionAtHead(30)
#l1.display()

l1.InsertionAtEnd(50)
l1.display()
