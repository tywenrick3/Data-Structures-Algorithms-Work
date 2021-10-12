class BinarySearchTreeMap:
    class item:
        def __init__(self, key, value = None):
            self.key = key
            self.value = value
    
    class Node:
        def __init__(self, item):
            self.data = item.value
            self.right = None
            self.left = None
            self.parent = None
        
        def num_children(self):
            count = 0
            if self.left is not None:
                count += 1
            if self.right is not None:
                count += 1
            return count
        
        def disconnect(self):
            self.data = None
            self.left = None
            self.right = None
            self.parent = None
    
    def __init__(self):
        self.root = None
        self.size = 0
    
    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0
    
    def __getitem__(self, key):
        node = self.find_node(key)
        if node is not None:
            return node.item.value
        raise KeyError("Key not found")
    
    def __setitem__(self, key, value):
        node = self.find_node(key)
        if node is not None:
            node.item.value = value
            return
        else:
            self.insert(key, value)
            return
        
    def __delitem__(self, key):
        node = self.find_node(key)
        if node is not None:
            return self.deleteNode(node)
        raise KeyError("Key is Not Found")
    
    def deleteNode(self, node):
        pass
        
    def insert(self, key, value):
        new_item = BinarySearchTreeMap.item(key, value)
        new_node = BinarySearchTreeMap.Node(new_item)
        parent = self.root
        currNode = self.root
        if parent.item.key < key:
            currNode = parent.right
        else:
            currNode = parent.left
            
        while parent is not None:
            if parent.item.key < key:
                parent = parent.right
            else:
                parent = parent.left
        
        if parent.item.key < key:
            parent.right = new_node
        else:
            parent.left = new_node
            
        new_node.parent = parent
        self.size += 1
        
                        
    def find_node(self, key):
        curr = self.root
        while curr is not None:
            if curr.item.key == key:
                return curr.item
            elif curr.item.key < key:
                curr = curr.right
            else:
                curr = curr.left
        return None
    
def main():
    bst = BinarySearchTreeMap()
    bst.insert()
    
    
    
    
    
main()