import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayDeque:

    INITIAL_CAPACITY = 10

    def __init__(self):
        self.data_arr = make_array(ArrayDeque.INITIAL_CAPACITY)
        self.num_of_items = 0
        self.front_ind = None
        self.back_ind = None

    def __len__(self):
        return self.num_of_items

    def is_empty(self):
        return self.num_of_items == 0
    
    def resize(self, new_size):
        new_arr = make_array(new_size)
        old_arr = self.data_arr
        old_index = self.front_ind

        for new_index in range(self.num_of_items):
            new_arr[new_index] = old_arr[old_index]
            old_index = (old_index+1)%len(old_arr)
        
        self.data_arr = new_arr

    def first(self):
        if self.data_arr.is_empty():
            raise Exception("Deque is empty!!!")
        return self.data_arr[self.front_ind]

    def last(self):
        if self.data_arr.is_empty():
            raise Exception("Deque is empty!!!")
        return self.data_arr[self.back_ind]

    def enqueue_first(self, elem):
        pass

    def enqueue_last(self, elem):
        if (self.num_of_items == len(self.data_arr)):
            self.resize(2*len(self.data_arr))
        end_ind = (self.front_ind+self.num_of_items) % len(self.data_arr)
        self.data_arr[end_ind] = elem
        self.num_of_items += 1

    def dequeue_first(self):
        if self.is_empty():
            raise Exception("Queue is Empty!!!")
        returned_item = self.data_arr[self.front_ind]
        self.data_arr[self.front_ind] = None
        self.front_ind = (self.front_ind+1) % len(self.data_arr)
        self.num_of_items -= 1
        if (self.num_of_items < len(self.data_arr) // 4 and len(self.data_arr) > ArrayDeque.initial_capacity):
            self.resize(len(self.data_arr)//2)
            
        return returned_item

    def dequeue_last(self):
        if self.is_empty():
            raise Exception("Queue is Empty!!!")
        returned_item = self.data_arr[self.back_ind]
        self.data_arr[self.back_ind] = None
        self.back_ind = (self.back_ind+1) % len(self.data_arr)
        self.num_of_items -= 1
        if (self.num_of_items < len(self.data_arr) // 4 and len(self.data_arr) > ArrayDeque.initial_capacity):
            self.resize(len(self.data_arr)//2)
            
        return returned_item

