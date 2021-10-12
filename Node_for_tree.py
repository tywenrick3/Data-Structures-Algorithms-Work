class Node:
    def __init__(self, data = None, left = None, right = None, parent = None):
        self.data = data
        self.left = left
        if self.left is not None:
            self.left.parent = self
        self.right = right
        if self.right is not None:
            self.right.parent = self
        self.parent = parent

#approach 1
#node_4 = Node(4)
#node_3 = Node(3)
#node_5 = Node(5)
#node_1 = Node(1)
#node_2 = Node(2)

#node_4.left = node_3
#node_4.right = node_5
#node_3.parent = node_4
#node_5.parent = node_4
#node_3.left = node_1
#node_3.right = node_2
#node_1.parent = node_3
#node_2.parent = node_3

#approach 2
node_1 = Node(1)
node_2 = Node(2)

node_3 = Node(3, node_1, node_2)

node_5 = Node(5)
node_4 = Node(4, node_3, node_5)
root = node_4