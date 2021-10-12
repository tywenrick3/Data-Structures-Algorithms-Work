class HoledStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [0] * self.capacity
        self.size = 0



    def __len__(self):
        return self.size


    def is_empty(self):
        return self.size == 0


    def push(self, e):  
        if self.size == self.capacity:
            self.data.pop(0)
            self.size -= 1
        self.data.append(e)
        self.size += 1  


    def pop(self):
        return_val = self.data.pop()
        self.size -= 1
        return return_val



    def top(self):
        return self.data[len(self.data)-1]


def main():
    s1 = HoledStack(5) 
    s1.push(4)
    s1.push(5)
    s1.push(10)
    s1.push(15)
    s1.pop()
    15
    s1.push(200)
    s1.push(500)
    s1.push(19) 
    len(s1)
    5
    s1.pop()
    19
    print(s1.data)
main()