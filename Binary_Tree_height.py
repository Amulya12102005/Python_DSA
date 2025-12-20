class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def PreOrder(Root):
    if Root == None:
        return
    print(Root.data, end=" ")
    PreOrder(Root.left)
    PreOrder(Root.right)
                                                                             # time complexity=O(n)
Root = Node(10)
Root.left = Node(20)
Root.right = Node(30)
Root.left.left = Node(40)
Root.left.right = Node(50)
Root.right.left = Node(60)
Root.right.right = Node(70)

PreOrder(Root)
print()




def height(root):
    if root == None:
        return -1
    else:
        return max(height(root.left), height(root.right)) + 1
print(height(Root))