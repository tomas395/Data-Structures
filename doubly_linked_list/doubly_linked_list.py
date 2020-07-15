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
        new_node = ListNode(value, None)
        self.length += 1
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        # create instance of ListNode with value
        # increment the DLL length attribute

        # if DLL is empty
            # set head and tail to the new node instance

        # if DLL is not empty
            # set new node's next to current head
            # set head's prev to new node
            # set head to the new node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        value = self.head.value
        self.length -= 1
        current = self.head
        if self.head.next is not None:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = None
            self.tail = None
            del current
        return value

        # store the value of the head
        # decrement the length of the DLL
        # delete the head
        # if head.next is not None
        # set head.next's prev to None
        # set head to head.next
        # else (if head.next is None)
        # set head to None
        # set tail to None

        # return the value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value, None)
        self.length += 1
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        # create instance of ListNode with value
        # increment the DLL length attribute

        # if DLL is empty
        # set head and tail to the new node instance

        # if DLL is not empty
        # set new node's prev to current tail
        # set tail's next to new node
        # set tail to the new node

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        value = self.tail.value
        # delete refers to an instance of the doublylinked list
        self.delete(self.tail)
        return value

        # store the value of the tail
        # decrement the length of the DLL
        # delete the tail
        # if tail.prev is not None
        # set tail.prev's next to None
        # set tail to tail.prev
        # else (if tail.prev is None)
        # set head to None
        # set tail to None

        # return the value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        current = node
        del node
        self.length -= 1
        self.add_to_head(current.value)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        current = node
        if current.prev is None:
            self.head = current.next
        del node
        self.length -= 1
        self.add_to_tail(current.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
# once the pointers are knocked off, it's essentially deleted and left to garbage collection?

    def delete(self, node):
        if self.head is None and self.tail is None:  # check if empty and if so, return
            return
        self.length -= 1
        if self.head == self.tail and node == self.head:
            self.head = None
            self.tail = None
        if self.head == node:
            self.head = node.next
            del node

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        max_value = self.head.value
        current = self.head
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value
