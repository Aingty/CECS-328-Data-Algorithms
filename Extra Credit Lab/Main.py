import sys

# Add Extra path for Window Machines below
sys.path.append('C:/Users/Aingty/Documents/GitHub Repositories/CECS-328-Data-Algorithms/Useful-Functions')
# Add Extra path for Mac Machines below
sys.path.append('/Users/Aingty/Applications/GitHub Repositories/CECS-328-Data-Algorithms/Useful-Functions')
sys.path.append('/Users/Aingty/Applications/GitHub Repositories/CECS-328-Data-Algorithms/Binary-Search-Tree')

from BSTClass import *
from DecisionMaking import *

keepingGoing = True
binaryTree = new BST()
print("Welcome to the Interactive Binary Tree Program!")
while keepingGoing:
    validOptions = [1,2,3,4,5,6]
    print("Please choose an option")
    print("\t1. Print Tree\n\t2. Print Tree's Height\n\t3. Insert\n\t4. Find\n\t5. Delete\n\t6. Quit")
    choice = input("\t\tYour Choice: ")
    validOptions = pickOption(validOptions, choice)

    if validOptions == 1:
        pass
    elif validOptions == 2:
        pass
    elif validOptions == 3:
        pass
    elif validOptions == 4:
        pass
    elif validOptions == 5:
        pass
    elif validOptions == 6:
        keepingGoing = False
print("Thank you for using Aingty's Binary Tree Program. Have a Wonderful rest of your day! :)")
