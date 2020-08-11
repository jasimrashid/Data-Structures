"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create a new node setting it to value
        node = ListNode(value)
        if self.head == None or self.tail == None:
            self.head = node
            self.tail = node
        else:
        # link node's next to head & link head's prev to new node
            self.head.prev = node
            node.next = self.head
            # update head to new new
            self.head = node

        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        val = self.head.value
        # remove head+1's prev to Null (do we have to set the head's next to null? )
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head.next.prev = None
            # point head to head +1
            self.head = self.head.next

        self.length -= 1
        return val
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        # create new node. # node prev to head. node next is null
        node = ListNode(value)
        if self.head is None or self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            # node head next to new node
            self.tail = node
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        val = self.tail.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            # tail's previous node's next: set to null (do we set tail's prev to nulL?)
            self.tail.prev.next = None
            # point tail to tail's previous node
            self.tail = self.tail.prev
            
        self.length -= 1
        
        return val
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
            
        found = False
        current_node = self.head
        while found == False:
            if current_node == node:
                found = True        
                if current_node != self.head:
                    if current_node == self.tail: # if current node is tail
                        current_node.prev.next = None
                        self.tail = current_node.prev
                    else: 
                        current_node.prev.next = current_node.next
                        current_node.next.prev = current_node.prev
                    current_node.next = self.head
                    self.head.prev = current_node
                    self.head = current_node
            else:
                found = False
                current_node = current_node.next
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        
        found = False
        current_node = self.head
        while found == False:
            if current_node == node:
                found = True        
                if current_node != self.tail:
                    if current_node == self.head: # if current node is head
                        current_node.next.prev = None
                        self.head = current_node.next
                    else: 
                        current_node.next.prev = current_node.prev
                        current_node.prev.next = current_node.next
                    current_node.prev = self.tail
                    self.tail.next = current_node
                    self.tail = current_node
            else:
                found = False
                current_node = current_node.next
        

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        
        # traverse the linked list to find the node "current node"

        # point current node's previous's node's next to current node's next node and vice versa
        found = False
        current_node = self.head
        while found == False:
            if current_node == node:
                found = True
                self.length -= 1
                print('condition: ',self.head == self.tail)        
                if self.head == self.tail:
                    print('hello')
                    self.head = None
                    self.tail = None
                elif current_node == self.head: # if current node is head
                    current_node.next.prev = None
                    self.head = current_node.next
                elif current_node == self.tail:
                    current_node.prev.next = None
                    self.tail = current_node.prev
                else: 
                    current_node.next.prev = current_node.prev
                    current_node.prev.next = current_node.next  
            else:
                found = False
                current_node = current_node.next
        

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        
        current_node = self.head
        max = current_node.value
        while True:
            if current_node.value > max:
                max = current_node.value
            if current_node.next is None:
                break
            else:
                current_node = current_node.next
        return max


node = ListNode(1)
ll = DoublyLinkedList(node)


ll.remove_from_head()
# self.assertIsNone(self.dll.head)
# self.assertIsNone(self.dll.tail)
# self.assertEqual(len(self.dll), 0)

ll.add_to_head(2)
# self.assertEqual(self.dll.head.value, 2)
# self.assertEqual(self.dll.tail.value, 2)
# self.assertEqual(len(self.dll), 1)

# self.assertEqual(self.dll.remove_from_head(), 2)

ll.remove_from_head()



# ll.remove_from_head()
# # self.assertIsNone(self.dll.head)
# # self.assertIsNone(self.dll.tail)
# # self.assertEqual(len(self.dll), 0)
# ll.add_to_head(2)
# print(ll.head.value)
# print(ll.tail.value)
# print(ll.length)
# breakpoint()

# ll.add_to_head(2)
# ll.add_to_head(4)
# ll.add_to_head(2)
# ll.add_to_head(0)
# print('max: ',ll.get_max())

# print(ll.head.value)
# print(ll.tail.value)
# print(ll.length)

# ll.add_to_tail(1)
# print(ll.head.value)
# print(ll.tail.value)
# print(ll.length)

# ll.add_to_tail('d')
# print(ll.head.value)
# print(ll.tail.value)
# print(ll.length)

# ll.remove_from_tail()
# print(ll.head.value)
# print(ll.tail.value)
# print(ll.length)

# ll.remove_from_head()
# print(ll.head.value)
# print(ll.tail.value)
# print(ll.length)


# ll.add_to_tail('b')
# ll.add_to_tail('c')
# print(ll.head.value)
# print(ll.tail.value)
# print(ll.length)

# # print("----")

# ll.move_to_front(ll.tail)
# print(ll.head.value)
# print(ll.tail.value)
# print(ll.length)

# ll.move_to_front(ll.tail)
# print(ll.head.value)
# print(ll.tail.value)
# print(ll.length)

# ll.move_to_front(ll.tail.prev)
# print(ll.head.value)
# print(ll.tail.value)
# print(ll.length)

# ll.move_to_front(ll.head)
# print(ll.head.value)
# print(ll.tail.value)
# print(ll.length)

# ll.move_to_front(ll.head.next)
# print(ll.head.value)
# print(ll.tail.value)
# print(ll.length)

# # ll.move_to_front(ll.tail)
# # print(ll.head.value)
# # print(ll.tail.value)
# # print(ll.length)

# # ll.move_to_front(ll.tail)
# # print(ll.head.value)
# # print(ll.tail.value)
# # print(ll.length)

# ll.move_to_end(ll.tail)
# print(ll.head.value)
# print(ll.tail.value)
# print(ll.length)

# print("-----")
# ll.move_to_end(ll.tail)
# print(ll.head.value)
# print(ll.tail.value)
# print(ll.length)


# ll.move_to_end(ll.head)
# print(ll.head.value)
# print(ll.tail.value)
# print(ll.length)

# ll.move_to_end(ll.head.next)
# print(ll.head.value)
# print(ll.tail.value)
# print(ll.length)

# ll.move_to_end(ll.tail.prev)
# print(ll.head.value)
# print(ll.tail.value)
# print(ll.length)

# ll.delete(ll.tail)
# print(ll.head.value)
# print(ll.tail.value)
# print(ll.length)

# ll.delete(ll.head)
# print(ll.head.value)
# print(ll.tail.value)
# print(ll.length)

# ll.delete(ll.head.next)
# print(ll.head.value)
# print(ll.tail.value)
# print(ll.length)

# ll.delete(ll.head)
# print(ll.head)
# print(ll.tail)
# print(ll.length)