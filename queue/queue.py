from singly_linked_list import LinkedList, Node
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


class Queue:
    def __init__(self):
        self.size = 0  # keeping track of the size of linkedlist
        # assigning the self.storage to the linkedlist we imported
        self.storage = LinkedList()

    def __len__(self):
        return self.size  # returning the length of the list

    def enqueue(self, value):  # adding a node to the head of linklist
        # passing through a value to the list that creates a node and assigns it to the head of the list
        self.storage.add_to_tail(value)
        self.size = self.size + 1

    def dequeue(self):
        if self.size > 0:
            self.size = self.size - 1  # now we're subtracting from the size of the list
            # this method moves a node from the current linked list
            return self.storage.remove_head()


# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.size += 1
#         self.storage.append(value)

#     def dequeue(self):
#         if self.size > 0:
#             self.size = self.size - 1
#             return self.storage.pop(0)
