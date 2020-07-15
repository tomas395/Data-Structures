
from singly_linked_list import LinkedList, Node
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
# Runtime complexity. Using a LinkedList will give us much better performance than using a a basic array.
# It has to do with shifting each item over whenever inserting or removing nodes.
# [] O(n) vs LL() O(1)


# (O)1
# class Stack:
#     def __init__(self):
#         self.size = 0  # keeping track of the size of linkedlist
#         # assigning the self.storage to the linkedlist we imported
#         self.storage = LinkedList()

#     def __len__(self):  # returning the length of the list
#         return self.size

#     def push(self, value):  # adding a node to the head of linklist
#         # passing through a value to the list that creates a node and assigns it to the head of the list
#         self.storage.add_to_tail(value)
#         self.size = self.size + 1

#     def pop(self):
#         if self.size > 0:
#             self.size = self.size - 1  # now we're subtracting from the size of the list
#         return self.storage.remove_tail()

# O(n)


class Stack:

    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size = self.size + 1

    def pop(self):
        if self.size > 0:
            self.size = self.size - 1
            return self.storage.pop()
