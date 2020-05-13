"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self): 
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""    
    def add_to_head(self, value): 
        if self.head:
            self.head.insert_before(value)
            self.head = self.head.prev
            self.length += 1
        else:
            self.__init__(node=ListNode(value))

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.head:
            if self.head.next is None:
                self.tail = None
            current_head = self.head.value
            self.head = self.head.next
            self.length -= 1
            return current_head
        else:
            return None

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    
    def add_to_tail(self, value):
        if self.tail:
            self.tail.insert_after(value)
            self.tail = self.tail.next
            self.length += 1
        else:
            self.__init__(node=ListNode(value))

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    
    def remove_from_tail(self):
        if self.tail:
            if self.tail.prev is None:
                self.head = None
            current_tail = self.tail.value
            self.tail = self.tail.prev
            self.length -= 1
            return current_tail
        else:
            return None

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        current_node = node
        node.delete()
        self.length -= 1
        self.add_to_head(current_node.value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):       
        current_node = node
        if current_node.prev is None:
            self.head = current_node.next
        node.delete()
        self.length -= 1
        self.add_to_tail(current_node.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node): # store incoming node in variable 
        if node.prev is None and node.next is None: # this node is the only one on the list 
            self.head = None # removing the value of both head and tail pointing their values to none 
            self.tail = None  
            self.length -= 1 
            return node.value # this value would be deleted/no longer connected to the list

        elif node.prev is None: # this checks if the incoming node is deleted from the head 
            self.head = node.next 
            node.delete()
            self.length -= 1 
            return node.value
        elif node.next is None: # this checks if the incoming node is deleted from the tail 
            self.tail = node.prev
            node.delete()
            self.length -= 1
            return node.value
        else: 
            node.delete() # removes nodes that are in between the head and tail of the list 
            self.length -= 1
            return node.value
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        max_value = self.head.value # assigning the var of max_value to be set according to the node's value
        current_node = self.head
        while current_node: # using a while loop on each node in the list and iterating over them to get the value of each individual node. if the value is > than the last, it will be set as the new max_value and compare itself to the next, only becoming the next new max_value if it was greater than the last, otherwise it will move to the next node on the list until it stops and returns itself.
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.next
        return max_value
