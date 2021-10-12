class ArrayStack:

    def __init__(self):
        self.data = []

    def __len__(self): #theta(1)
        return len(self.data)

    def is_empty(self): #theta(1)
        return len(self.data) == 0

    def push(self, item): #amortized theta(1)
        self.data.append(item)

    def pop(self): #amortized theta(1)
        if (self.is_empty()):
            raise Exception("Stack is Empty!!!")
        return self.data.pop()

    def top(self): #
        if (self.is_empty()):
            raise Exception("Stack is Empty!!!")
        return self.data[-1]
    
def main():
    def flatten_list(lst):
        s = ArrayStack()
        for element in lst:
            if isinstance(element, list):
                flattened = flatten_list(element)
                for i in range(len(flattened)):
                    s.push(flattened[i])
            else:
                s.push(element)
        lst1 = []
        while not s.is_empty():
            lst1.insert(0, s.pop())
        return lst1
        
                    
    print(flatten_list([ [[[0]]], [1, 2], 3, [4, [5, 6, [7]], 8], 9])) 

main()