"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack_using_array:
    def __init__(self):
        self.size = 0
        self.storage = []
    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.append(value)

    def pop(self):
        if self.size != 0:
            self.size -= 1
            # val = self.storage.pop(len(self.storage)-1)
            return self.storage.pop(len(self.storage)-1)
        else:
            return None

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size != 0:
            self.size -= 1
            # val = self.storage.tail.get_value()
            return self.storage.remove_tail()
        else:
            return None

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None or self.tail is None:
            self.head = new_node
            self.tail = new_node

        else:
            val = self.head.get_value()
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_tail(self):
        if self.head is None and self.tail is None:
            return None

        if self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val

        else:
            val = self.tail.get_value()
            current = self.head
            while current.get_next() != self.tail:
                current = current.get_next()
            self.tail = current
            self.tail.set_next(None)
            return val

    def remove_head(self):
        if self.head is None and self.tail is None:
            return None

        elif self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val
        else:
            val = self.head.get_value()
            self.head = self.head.get_next()
            return val

        


