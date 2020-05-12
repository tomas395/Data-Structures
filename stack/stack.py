from linked_list import LinkedList, Node
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
class Stack:
    def __init__(self):
        self.size = 0 #keeping track of the size of linkedlist
        self.storage = LinkedList() #assigning the self.storage to the linkedlist we imported

    def __len__(self):   
        return self.size


    def push(self, value): # adding a node to the head of linklist
        self.storage.add_to_head(value) # passing through a value to the list that creates a node and assigns it to the head of the list
        self.size = self.size +1 

    def pop(self):
        if self.size > 0:
            self.size = self.size -1 # now we're subtracting from the size of the list
        return self.storage.remove_from_head()


# This is for the array portion of the stack
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.append(value)
#         self.size = self.size +1

#     def pop(self):
#         if self.size > 0:
#             self.size = self.size -1
#             return self.storage.pop()
#         else:
#             return None 
