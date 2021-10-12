import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayList:
    def __init__(self):
        self.data_arr = make_array(1)
        self.n = 0
        self.capacity = 1

    def __len__(self): #len(lst) # theta(1)
        return self.n

    def append(self, val):# amortized theta(1)
        if (self.n == self.capacity):
            self.resize(2*self.capacity)
        self.data_arr[self.n]= val
        self.n += 1

    def resize(self, new_size): #memory limitation,
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data_arr[i]
        self.data_arr = new_array
        self.capacity = new_size

    def __getitem__(self, ind):
        if ind <0:
            ind = self.n + ind
        if (not(0<=ind<=self.n-1)):
            raise IndexError("ArrayList index out of range!!!")
            
        return self.data_arr[ind]

    def __setitem__(self, ind, val):
        if ind <0:
            ind = self.n + ind
        if (not(0<=ind<=self.n-1)):
            raise IndexError("ArrayList index out of range!!!")
        self.data_arr[ind] = val

    def __iter__(self):
        for i in range(self.n):
            yield self.data_arr[i]

    def extend(self, iter_collection):
        for each in iter_collection:
            self.append(each)
        
    def index(self, val):
        for i in range(self.n):
            if (self[i]==val):
                return i
        return None

    def count(self, val):
        cnt = 0
        for each in self:
            if each == val:
                cnt += 1
        return cnt
        
    def is_empty(self):
        return self.n == 0
    
    def reverse(self):
        for i in range(len(self)//2):
            j = len(self)-1-i
            self.data_arr[i],self.data_arr[j] = self.data_arr[j], self.data_arr[i]

    def __repr__(self):
        data_as_strings = [str(self.data_arr[i]) for i in range(self.n)]
        return '[' + ', '.join(data_as_strings) + ']'
            
    def copy(self):
        # Return a shallow copy of the ArrayList.
        # your code
        new_arr = make_array(self.capacity)
        for i in range(self.n):
            new_arr[i] = self.data_arr[i]
        return new_arr
        #time complexity is theta(n) becuase it loops through all the elements in the orginal arraylist to refernce for the new copied array
        

mlst1 = ArrayList()
for i in range(5):
    mlst1.append(i)

mlst2 = mlst1.copy()
mlst2[0] = 300

print(mlst2[0])
print("mlst1: ",mlst1) # mlst1:  [0, 1, 2, 3, 4]
print("mlst2: ",mlst2) # mlst2:  [300, 1, 2, 3, 4]


