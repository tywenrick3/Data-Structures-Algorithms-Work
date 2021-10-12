import random

class BinarySearchTreeMap:

    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value


    class Node:
        def __init__(self, item):
            self.item = item
            self.parent = None
            self.left = None
            self.right = None

        def num_children(self):
            count = 0
            if (self.left is not None):
                count += 1
            if (self.right is not None):
                count += 1
            return count

        def disconnect(self):
            self.item = None
            self.parent = None
            self.left = None
            self.right = None


    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0
    
    def __getitem__(self, key):
        node = self.find_node(key)
        
        if node is not None:
            return node.item.value
        else:
            raise KeyError(str(key)+ " not found!!!")
        
    def find_node(self, key):
        
        currNode = self.root
        
        while currNode is not None:
            if currNode.item.key == key:
                return currNode
            elif currNode.item.key > key:
                currNode = currNode.left
            else:
                currNode = currNode.right
        
        return None
    
    def __setitem__(self, key, value=None):
        
        node = self.find_node(key)
        
        if node is not None:
            node.item.value = value
        else:
            self.insert(key, value)
    
    # we need to create a new node
    def insert(self, key, value=None):
        item = BinarySearchTreeMap.Item(key,value)
        new_node = BinarySearchTreeMap.Node(item)
        
        if (self.is_empty()):
            self.root = new_node
            self.size = 1
        else:
            parent = self.root
            
            if key < self.root.item.key:
                currNode = self.root.left
            else:
                currNode = self.root.right
                
            while currNode is not None:
                parent = currNode
                if key < currNode.item.key:
                    currNode = currNode.left
                else:
                    currNode = currNode.right
                    
            
            if key < parent.item.key:
                parent.left = new_node
            else:
                
                parent.right = new_node
            
            new_node.parent = parent
            self.size += 1

    def __delitem__(self, key):
        node = self.find_node(key)
        if node is None:
            raise KeyError(str(key)+ " not found!!!")
        else:
            self.delete_node(node)
            
            
    def delete_node(self, node_to_delete):
        item = node_to_delete.item
        num_of_children = node_to_delete.num_children()
        
        if node_to_delete is self.root:
            
            if num_of_children ==0:
                self.root = None
                self.size = 0
                node_to_delete.disconnect()
                
            elif num_of_children == 1:
                if self.root.left is not None:
                    self.root = self.root.left
                else:
                    self.root = self.root.right
                    
                self.root.parent = None
                node_to_delete.disconnect()
                self.size -= 1
                
            else:
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                
                self.delete_node(max_of_left)
        else:
            
            if num_of_children == 0:
                
                parent = node_to_delete.parent
                
                if node_to_delete is parent.left:
                    parent.left = None
                else:
                    parent.right = None
                    
                node_to_delete.disconnect()
                self.size -= 1
                
            elif num_of_children == 1:
                
                parent = node_to_delete.parent
                
                if node_to_delete.left is not None:
                    child = node_to_delete.left
                else:
                    child = node_to_delete.right
                    
                if node_to_delete is parent.left:
                    parent.left = child
                else:
                    parent.right = child
                    
                child.parent = parent
                node_to_delete.disconnect()
                self.size -= 1
                
            else:
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.delete_node(max_of_left)
        
        return item
        
     
    def subtree_max(self, curr_root):
        node = curr_root
        while node.right is not None:
            node = node.right
        
        return node

    def subtree_min(self, curr_root):
        node = curr_root
        if node.left is None:
            return node
        return self.subtree_min(node.left)

    def inorder(self):
        def subtree_inorder(root):
            if (root is None):
                pass
            else:
                yield from subtree_inorder(root.left)
                yield root
                yield from subtree_inorder(root.right)

        yield from subtree_inorder(self.root)


    def __iter__(self):
        for node in self.inorder():
            yield node.item.key
        
bst = BinarySearchTreeMap()
lst = list(range(100))
random.shuffle(lst)
lst = lst[:100]
#print(lst)
for i in lst:
    bst.insert(i)

print(bst)
print()
        
#for k in bst:
#    print(k, end=" ")
#print()

#random.shuffle(lst)
#print(lst)
#for i in lst:
#    del bst[i]
    #print(i)
#    for k in bst:
        #print(k, end=" ")
    #print()
    #print()
                
            
        
            
        
        
