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
        root = self  # Assigning the self to root to help me visualize. not at all necessary and just for me
        new_node = BSTNode(value)
        if value < root.value:  # If a nodes value is found to be less than the roots, it will put it to the left, if theres nothing there it will make a new node in it's place
            if root.left is None:
                root.left = new_node
            else:
                root.left.insert(value)
        elif value >= root.value:  # Same as above except if it's higher, it will be placed to the right unless theres nothing in it, in that case it will be the new_node_right
            if root.right is None:
                root.right = new_node
            else:
                root.right.insert(value)  # ayyyye it passed ♥ ... i think
                # I need to figure out what BSTs do with duplicate values or if it's equal to the root or parent

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # when we start searching, self will be the root
        # compare the target against self
        #
        # Criteria for returning False: we know we need to go in one direction
        # but there's nothing in the left or right direction
        if target == self.value:
            return True
        if target < self.value:
            # go left if left is a BSTNode
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            # go right if right is a BSTNode
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        root = self
        if root.right is None:  # If the right side is empty, then give the current.value
            return root.value
        else:  # If there is something in the right side, then keep going down until each max_value is found and return it
            return root.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        root = self
        # If there is something in root.left, execute the (fn) forEach on it
        if root.left:
            root.left.for_each(fn)
        if root.right:
            # If there is something in root.right, execute the (fn) forEach on it like self.left ↑
            root.right.for_each(fn)
        fn(root.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
