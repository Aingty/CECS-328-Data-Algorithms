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
    