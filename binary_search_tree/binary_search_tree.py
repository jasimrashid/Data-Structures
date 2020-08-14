"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            # is there a left child
            if self.left: # same as self.left is not None:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else: # go right
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        else:
            if target < self.value:
                if self.left is None:
                    return False
                else:
                    return self.left.contains(target)
            else:
                if self.right is None:
                    return False
                else:
                    return self.right.contains(target)
                    

    # Return the maximum value found in the tree
    def get_max(self):
        max = self.value
        if self.right is None:
            return max
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # breakpoint()
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
        # if self.left is None  or self.right is None: #this is a leaf
        return fn(self.value)

        # this can be done iteratively using a stack
        stack = []
        # add root node to stack
        stack.append(self)

        # continue popping from our stack so long a there are nodes in it
        # depth first
        while len(stack) > 0:
            current_node = stack.pop()
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            fn(current_node.value)

        # breath first

        from collections import deque
        q = deque()
        q.append(self)

        while len(q) > 0:
            current_node = q.popleft()

            # check if node has children
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)

            fn(current_node.value)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # if self.left is None and self.right is None:
        #     print(self.value)
        # else:
        if self.left:
            self.left.in_order_print()

        print(self.value)

        if self.right:
            self.right.in_order_print()


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        from collections import deque
        q = deque()
        q.append(self)
        while len(q) != 0:
            current_node = q.popleft()
            print(current_node.value)
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)



    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        stack = []
        stack.append(self)
        while len(stack) != 0:
            current_node = stack.pop()
            print(current_node.value)
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    # pre-order DFT is the default dft ~ so same as dft_print
    def pre_order_dft(self):
        print(self.value)
        if self.left:
            self.left.pre_order_dft()
        if self.right:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        if self.left:
            self.left.post_order_dft()
        if self.right:
            self.right.post_order_dft()
        print(self.value)
        

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(8)

bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(4) #
bst.insert(7) #
bst.insert(14)
bst.insert(13)

print(bst.contains(11))

print('in order print')
bst.in_order_print()

print()

print('bft')
bst.bft_print() 
# breakpoint()
print('dft')
bst.dft_print()

print('pre-order dft')
bst.pre_order_dft()

print('post-order dft')
bst.post_order_dft()



# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  


# arr = []
# cb = lambda x: arr.append(x)
# cb2 = lambda x: arr.append(x)
# cb(1)
# cb(2)



# breakpoint()