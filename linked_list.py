class SinglyLinkedList:

    class Node:
        def __init__(self, elem = None, next = None):
            self.data = None
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add_first(self, elem):
        new_node = self.Node(elem)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def delete_first(self):
        if self.is_empty():
            raise Exception("LinkedList is Empty!!!")
        return_val = self.head.data
        self.head = self.head.next
        self.size -= 1
        return return_val

ll1 = SinglyLinkedList()
ll1.add_first(1)
ll1.add_first(2)
ll1.add_first(3)

cursor = ll1.head

while cursor is not None:
    print(cursor.data, end = " ")
    cursor = cursor.next

print()

ll1.delete_first()

