class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


Root = Node(18)


def BSTInsertion(Root, data):
    if Root == None:
        return Node(data)
    if Root.data < data:
        Root.right = BSTInsertion(Root.right, data)
    else:
        Root.left = BSTInsertion(Root.left, data)
    return Root


def InOrder(Root):
    if Root == None:
        return
    InOrder(Root.left)
    print(Root.data, end=" ")
    InOrder(Root.right)

def BSTsearch(Root, key):
    if Root == None:
        print("Element not found")
        return
    if Root.data == key:
        print("Element found")
        return
    if Root.data < key:
        BSTsearch(Root.right, key)
    else:
        BSTsearch(Root.left, key)




BSTInsertion(Root, 15)
BSTInsertion(Root, 22)
BSTInsertion(Root, 88)
BSTInsertion(Root, 77)
BSTInsertion(Root, 42)
BSTInsertion(Root, 60)
BSTInsertion(Root, 14)
BSTInsertion(Root, 13)
BSTInsertion(Root, 50)
InOrder(Root)
BSTsearch(Root, 42)

