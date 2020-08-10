"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?


   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


# from pd.singly_linked_list.singly_linked_list import LinkedList, Node

# from singly_linked_list.singly_linked_list import LinkedList, Node

# from singly_linked_list.singly_linked_list import LinkedList, Node
from singly_linked_list import LinkedList

class Queue_using_arrays:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.append(value)
        # self.storage.insert(0,value) #then remove from the end of the array
        self.size += 1

    def dequeue(self):
        if self.size != 0:
            self.size -= 1
            return self.storage.pop(0)
        else:
            return None

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size != 0:
            self.size -= 1
            return self.storage.remove_head()
        else:
            return None

# class Node:
#     def __init__(self, value, next_node=None):
#         self.value = value
#         self.next_node = next_node

#     def get_value(self):
#         return self.value

#     def get_next(self):
#         return self.next_node

#     def set_next(self, new_next):
#         self.next_node = new_next

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None    

#     def add_to_tail(self, value):
#         new_node = Node(value)
#         if self.head is None or self.tail is None:
#             self.head = new_node
#             self.tail = new_node

#         else:
#             val = self.head.get_value()
#             self.tail.set_next(new_node)
#             self.tail = new_node

#     def remove_tail(self):
#         if self.head is None and self.tail is None:
#             return None

#         if self.head == self.tail:
#             val = self.head.get_value()
#             self.head = None
#             self.tail = None
#             return val

#         else:
#             val = self.tail.get_value()
#             current = self.head
#             while current.get_next() != self.tail:
#                 current = current.get_next()
#             self.tail = current
#             self.tail.set_next(None)
#             return val

#     def remove_head(self):
#         if self.head is None and self.tail is None:
#             return None

#         elif self.head == self.tail:
#             val = self.head.get_value()
#             self.head = None
#             self.tail = None
#             return val
#         else:
#             val = self.head.get_value()
#             self.head = self.head.get_next()
#             return val



q = Queue()
q.enqueue(1)
q.enqueue('a')
print(q.storage)
q.dequeue()
print(q.storage)
q.dequeue()
print(q.storage)
q.dequeue()
print(q.storage)
q.enqueue(3)
q.enqueue(4)
print(q.storage)



