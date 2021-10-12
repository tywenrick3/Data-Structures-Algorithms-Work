import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayQueue:

    initial_capacity = 10

    def __init__(self):
        
        self.data_arr = make_array(ArrayQueue.initial_capacity)
        self.num_of_items = 0
        self.front_ind = None

    def __len__(self): #theta(1)
        return self.num_of_items
    
    def is_empty(self): #theta(1)
        return self.num_of_items == 0
    
    def resize(self, new_size):
        new_arr = make_array(new_size)
        old_arr = self.data_arr
        old_index = self.front_ind

        for new_index in range(self.num_of_items):
            new_arr[new_index] = old_arr[old_index]
            old_index = (old_index+1)%len(old_arr)
        
        self.data_arr = new_arr
    
    def enqueue(self, item): #amortized theta(1)
        if (self.num_of_items == len(self.data_arr)):
            self.resize(2*len(self.data_arr))
        end_ind = (self.front_ind+self.num_of_items) % len(self.data_arr)
        self.data_arr[end_ind] = item
        self.num_of_items += 1


    def dequeue(self): #amortized theta(n)
        if self.is_empty():
            raise Exception("Queue is Empty!!!")
        returned_item = self.data_arr[self.front_ind]
        self.data_arr[self.front_ind] = None
        self.front_ind = (self.front_ind+1) % len(self.data_arr)
        self.num_of_items -= 1
        if (self.num_of_items < len(self.data_arr) // 4 and len(self.data_arr) > ArrayQueue.initial_capacity):
            self.resize(len(self.data_arr)//2)
            
        return returned_item
        
    
    def first(self): #theta(1)
        if self.is_empty():
            raise Exception("Queue is Empty!!!")
        return self.data_arr[self.front_ind]