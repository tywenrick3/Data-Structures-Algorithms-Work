from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack

class LinkedBinaryTree:

    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.parent = None
            self.left = left
            if (self.left is not None):
                self.left.parent = self
            self.right = right
            if (self.right is not None):
                self.right.parent = self

    def __init__(self, root=None):
        self.root = root
        self.size = self.count_nodes()

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0


    def count_nodes(self):
        def subtree_count(root):
            if (root is None):
                return 0
            else:
                left_count = subtree_count(root.left)
                right_count = subtree_count(root.right)
                return 1 + left_count + right_count

        return subtree_count(self.root)


    def sum(self):
        def subtree_sum(root):
            if (root is None):
                return 0
            else:
                left_sum = subtree_sum(root.left)
                right_sum = subtree_sum(root.right)
                return root.data + left_sum + right_sum

        return subtree_sum(self.root)


    def height(self):
        def subtree_height(root):
            if (root.left is None and root.right is None):
                return 0
            elif (root.left is None):
                return 1 + subtree_height(root.right)
            elif (root.right is None):
                return 1 + subtree_height(root.left)
            else:
                left_height = subtree_height(root.left)
                right_height = subtree_height(root.right)
                return 1 + max(left_height, right_height)

        if(self.is_empty()):
            raise Exception("Tree is empty")
        return subtree_height(self.root)


    def preorder(self):
        def subtree_preorder(root):
            if (root is None):
                pass
            else:
                yield root
                yield from subtree_preorder(root.left)
                yield from subtree_preorder(root.right)

        yield from subtree_preorder(self.root)


    def postorder(self):
        def subtree_postorder(root):
            if (root is None):
                pass
            else:
                yield from subtree_postorder(root.left)
                yield from subtree_postorder(root.right)
                yield root

        yield from subtree_postorder(self.root)


    def inorder(self):
        def subtree_inorder(root):
            if (root is None):
                pass
            else:
                yield from subtree_inorder(root.left)
                yield root
                yield from subtree_inorder(root.right)

        yield from subtree_inorder(self.root)


    def breadth_first(self):
        if (self.is_empty()):
            return
        line = ArrayQueue()
        line.enqueue(self.root)
        while (line.is_empty() == False):
            curr_node = line.dequeue()
            yield curr_node
            if (curr_node.left is not None):
                line.enqueue(curr_node.left)
            if (curr_node.right is not None):
                line.enqueue(curr_node.right)
    
    def level_by_level_order_print(self):
        if (self.is_empty()):
            raise Exception("Binary Tree is Empty!!!")
        line = ArrayQueue()
        line.enqueue(self.root)
        while not line.is_empty():
            for i in range(len(line)):
                curr_node = line.dequeue()
                print(curr_node.data, end=" ")
                if (curr_node.left is not None):
                    line.enqueue(curr_node.left)
                if (curr_node.right is not None):
                    line.enqueue(curr_node.right)
            print()

    def __iter__(self):
        for node in self.breadth_first():
            yield node.data
    
    def preorder_iter(self):
        if self.is_empty():
            raise Exception("Binary Tree is Empty!!!")
        s = ArrayStack()
        s.push(self.root)
        while not s.is_empty():
            curr_node = s.pop()
            if curr_node.right is not None:
                s.push(curr_node.right)
            if curr_node.left is not None:
                s.push(curr_node.left)

    
    def is_BST(self, linkedBinaryTree):
        pass
            
node_4 = LinkedBinaryTree.Node(4)
node_5 = LinkedBinaryTree.Node(5)
node_6 = LinkedBinaryTree.Node(6)
node_2 = LinkedBinaryTree.Node(2, node_4, node_5)
node_3 = LinkedBinaryTree.Node(3, None, node_6)           
node_1 = LinkedBinaryTree.Node(1, node_2, node_3)


root = LinkedBinaryTree(node_1)

tree = LinkedBinaryTree(root)

print(tree.breadth_first())


          

