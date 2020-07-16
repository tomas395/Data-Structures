from queue import Queue
from stack import Stack
# from collections import deque
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
        # Case 1: value is less than self.value
        if value < self.value:
            # If there is no left child, insert value here
            if self.left is None:
                self.left = BSTNode(value)
            else:
                # Repeat the process on left subtree
                self.left.insert(value)

        # Case 2: value is greater than or equal self.value
        elif value >= self.value:
            # If there is no right child, insert value here
            if self.right is None:
                self.right = BSTNode(value)
            else:
                # Repeat the process on right subtree
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # Case 1: self.value is equal to the target
        if self.value == target:
            return True
        # Case 2: target is less than self.value
        if target < self.value:
            # if self.left is None, it isn't in the tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # Case 3: otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        max_val = self
        if max_val.right is None:  # If the right side is empty, then give the current.value
            return max_val.value
        else:  # If there is something in the right side, then keep going down until each max_value is found and return it
            return max_val.right.get_max()

            # OR
        # max_value = self.value
        # current = self
        # while current:
        #     if current.value > max_value:
        #         max_value = current.value
        #     current = current.right
        # return max_value


# anything i can express with a loop i can also use for recursion
# linear time will be the worst case scenario for a binary tree. O(n)
    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        fn(self.value)
        # If there is something in self.left, execute the (fn) forEach on it
        if self.left:
            self.left.for_each(fn)
        # If there is something in self.right, execute the (fn) forEach on it like self.left ↑
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

# they dictate the order you visit the nodes in
# inorder - left self right
# preorder - self, left right
# and postorder left right self
# level order maybe not recursivly?
#

    def in_order_print(self, node):
        # if the current node is None
        # we know we've reached the end of a recursion
        # (base case) we want to return
        if self is None:
            return

        # check if we can "move left"
        if node.left is not None:
            node.left.in_order_print(node.left)

        # visit the node by printing its value
        print(node.value)

        # check if we can "move right"
        if node.right is not None:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)

        while queue:
            current_node = queue.dequeue()
            print(current_node.value)

            if current_node.left is not None:
                queue.enqueue(current_node.left)

            if current_node.right is not None:
                queue.enqueue(current_node.right)

        # You should import the queue class from earlier in the
        # week and use that class to implement this method
        # Use a queue to form a "line"
        # for the nodes to "get in"

        # start by placing the root in the queue

        # need a while loop to iterate
        # what are we checking in the while statement?
        # while length of queue is greater than 0
        # dequeue item from front of queue
        # print that item

        # place current item's left node in queue if not None
        # place current item's right node in queue if not None

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        stack = Stack()
        stack.push(node)

        while stack:
            current_node = stack.pop()
            print(current_node.value)

            if current_node.left is not None:
                stack.push(current_node.left)

            if current_node.right is not None:
                stack.push(current_node.right)

        # initialize an empty stack
        # push the root node onto the stack

        # need a while loop to manager our iteration
        # if stack is not empty enter the while loop
        # pop top item off the stack
        # print that item's value

        # if there is a right subtree
        # push right item onto the stack

        # if there is a left subtree
        # push left item onto the stack

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
