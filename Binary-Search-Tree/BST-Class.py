from BTS-Node-Class import Node


class BST(object):
    """
    This is the Binary Search Tree class used for CECS 328. It is composed of custom node class.
    """

    def _init_(self):
        """
        Constructor of Binary Search Tree and set the root of the tree to null.
        """
        self.root = null

    def getHeight(self):
        """
        Return the height of the Binary Search Tree
        """
        pass

    def insert(self, value):
        """
        Insert *value* into the Binary Search Tree, following Binary Tree's insertion rule.
        """
        if self.root == null:
            self.root = Node(value)
        else:
            
