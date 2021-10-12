class flipstack:
    def __init__(self):
        self.data = []
    
    def __len__(self):
        return len(self.data)
    
    def is_empty(self):
        return len(self.data) == 0
    
    def push(self, value):
        self.data.append(value)
    
    def pop(self):
        return_val = self.data.pop()
        return return_val
    
    def flipstack(self):
        temp = flipstack()
        while not self.is_empty():
            x = self.data.pop()
            temp.push(x)
        self.data = temp
        
    def insert_bottom(self, val):
        if self.is_empty():
            self.push(val)
        else:
            popped = self.pop()
            self.insert_bottom(val)
            self.push(popped)
    
    def flipstack2(self):
        if self.is_empty():
            return
        else:
            popped = self.pop()
            self.flipstack2()
            self.insert_bottom(popped)
        
        
    def top(self):
        return self.data[len(self.data)-1]
    
    def __iter__(self):
        for i in range(len(self)):
            yield self.data[i]
    
    def __repr__(self):
        return "[" + ", ".join([str(elem) for elem in self.data]) + "]"
    
    def show(self):
        for value in reversed(self.Elements):
            print(value)
    

def main():
    s = flipstack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    print(s)
    s.flipstack2()
    print(s)
    s.pop()
    print(s)
   
   
        
main()
        