from BTSNodeClass import *


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
            posFound = False
            temp = self.root
            while !posFound:
                if value <= temp.getValue() and temp.getLeftChild() == null:
                    temp.setLeftChild(Node(value))
                    posFound = True
                elif value > temp.getValue() and temp.getRightChild() == null:
                    temp.setRightChild(Node(value))
                    posFound = True
                elif value <= temp.getLeftChild():
                    temp = temp.getLeftChild()
                elif value > temp.getRightChild():
                    temp = temp.getRightChild()
    
    def searchNode(self,key):
        """
        Fucntion that returns True if *key* exists in the Binary Tree. Return False otherwise.
        """
        if self.root == null:
            return False
        else:
            nodeFound = False
            temp = self.root
            while !nodeFound:
                if key == temp.getValue():
                    return True
                elif key < temp.getValue() and temp.getLeftChild() != null:
                    temp = temp.getLeftChild()
                elif key > temp.getValue() and temp.getRightChild() != null:
                    temp = temp.getRightChild()
                else:
                    return False
                    
