class Node(object):
    """
    Custom Node class to be use with Binary Search Tree class.
    """

    def __init__(self,value):
        """
        Constructer for Node class with initial value of *value*.
        """
        self.value = value
        self.leftChild = null
        self.rightChild = null

    def setLeftChild(self,left):
        """
        Function to set the left child of the node to *left*.
        """
        self.leftChild = left
    
    def setRightChild(self,right):
        """
        Function to set the right child of the node to *right*.
        """
        self.rightChild = right

    def getLeftChild(self):
        """
        Function to return the left child of the node.
        """
        return self.leftChild

    def getRightChild(self):
        """
        Function to return the right child of the node.
        """
        return self.rightChild

    def getNodeValue(self):
        """
        Function to return the node's value.
        """
        return self.value

    