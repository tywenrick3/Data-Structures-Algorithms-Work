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




def assign_parents_correctly(bin_tree):
    def assign_parents_node(curr_node):
        if curr_node.left is not None:
            curr_node.left.parent = curr_node
            assign_parents_node(curr_node.left)
            
        if curr_node.right is not None:
            curr_node.right.parent = curr_node
            assign_parents_node(curr_node.right)
    
    assign_parents_node(bin_tree.root)
    
    