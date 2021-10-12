from ArrayQueue import ArrayQueue

class LinkedBinaryTree:
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
            
            
    def __init__(self, root = None):
        self.root = root
        self.size = self.count_nodes()
        
        
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
        
        
    def count_nodes(self):
        def subtree_count_nodes(node):
            if node is None:
                return 0
            else:
                left_count = subtree_count_nodes(node.left)
                right_count = subtree_count_nodes(node.right)
                
                return 1+left_count+right_count
        
        return subtree_count_nodes(self.root)
    
    def sum(self):
        def subtree_sum(node):
            if node is None:
                return 0
            else:
                left_sum = subtree_sum(node.left)
                right_sum = subtree_sum(node.right)
                
                return node.data+left_sum+right_sum
        
        return subtree_sum(self.root)
    
    def height(self):
        def subtree_height(node):
            
            if node.left is None and node.right is None:
                return 0
            elif node.left is None:
                return 1+subtree_height(node.right)
            elif node.right is None:
                return 1+subtree_height(node.left)
            else:
                1+max(subtree_height(node.left), subtree_height(node.right))
                
        if (self.is_empty()):
            raise Exception("Tree is Empty!!!")
            
        return subtree_height(self.root)
    
    def depth(self, node):
        if node is self.root:
            return 0
        else:
            return 1+self.depth(node.parent)
        
    def preorder(self):
        def subtree_preorder(node):
            if node is None:
                pass
            else: 
                yield node
                yield from subtree_preorder(node.left)
                yield from subtree_preorder(node.right)

        yield from subtree_preorder(self.root)        
        
    def postorder(self):
        def subtree_postorder(node):
            if node is None:
                pass
            
            else:
                yield from subtree_postorder(node.left)
                yield from subtree_postorder(node.right)
                yield node

        yield from subtree_postorder(self.root)
        
    def inorder(self):
        def subtree_inorder(node):
            if node is None:
                pass
            
            else:
                yield from subtree_inorder(node.left)
                yield node
                yield from subtree_inorder(node.right)
            
        yield from subtree_inorder(self.root)
    
    def levelorder(self):
        if (self.is_empty()):
            raise Exception("BinaryTree is Empty!!!")
        q = ArrayQueue()
        q.enqueue(self.root)
        while not q.is_empty():
            temp = q.dequeue()
            yield temp
            if temp.left is not None:
                q.enqueue(temp.left)
                
            if temp.right is not None:
                q.enqueue(temp.right)
        
        
    def __iter__(self):
        for each in self.preorder():
            yield each.data


def eval_exp_tree(exp_tree):
    def subtree_eval(node):
        if (isinstance(node.data,(int,float))):
            return node.data
        else:
            left_arg = subtree_eval(node.left)
            right_arg = subtree_eval(node.right)
            
            if (node.data == '+'):
                return left_arg + right_arg
            elif (node.data == '-'):
                return left_arg - right_arg
            elif (node.data == '*'):
                return left_arg * right_arg
            elif (node.data == '/'):
                if (right_arg == 0):
                    raise ZeroDivisionError()    
                return left_arg / right_arg
            else:
                raise Exception("Unsupported Operation!!!")
    return subtree_eval(exp_tree.root)          

    
def tests():   
    node_5 = LinkedBinaryTree.Node(5)   
    node_2 = LinkedBinaryTree.Node(2)

    node_mul = LinkedBinaryTree.Node('*',node_5,node_2)

    node_3 = LinkedBinaryTree.Node(3)
    node_1 = LinkedBinaryTree.Node(1)
    node_min = LinkedBinaryTree.Node('-', node_3, node_1)

    root = LinkedBinaryTree.Node('+', node_mul, node_min)     

    print(root.data)        
    expression_tree = LinkedBinaryTree(root)

    for each in expression_tree:
        print(each, end = " ")

    print()    
    print(eval_exp_tree(expression_tree))

tests()
    

class solution:
    def max_depth(self, root):
        if not root:
            return 0
        depth = 0
        q = []
        q.append(root)
        while q:
            depth += 1
            temp = []
            for node in q:
                if node.left is not None:
                    temp.append(node.left)
                if node.right is not None:
                    temp.append(node.right)
            q = temp
        return depth

