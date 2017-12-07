import sys

# Add Extra path for Window Machines below
sys.path.append('C:/Users/Aingty/Documents/GitHub Repositories/CECS-328-Data-Algorithms/Useful-Functions')
# Add Extra path for Mac Machines below
sys.path.append('/Users/Aingty/Applications/GitHub Repositories/CECS-328-Data-Algorithms/Useful-Functions')
sys.path.append('/Users/Aingty/Applications/GitHub Repositories/CECS-328-Data-Algorithms/Binary-Search-Tree')

from BSTClass import *
from DecisionMaking import *

keepingGoing = True
binaryTree = BST()
print("Welcome to the Interactive Binary Tree Program!")
print("Please choose an option")
while keepingGoing:
    validOptions = [1,2,3,4,5,6]
    print("\t1. Print Tree\n\t2. Print Tree's Height\n\t3. Insert\n\t4. Find\n\t5. Delete\n\t6. Quit")
    choice = input("\t\tYour Choice: ")
    if choice.isdigit():
        choice = int(choice)
    else:
        print ("Invalid Choice!!! Please input a number!")
        continue
    choice = pickOption(validOptions, choice)
    print (choice)
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        keepingGoing = False
    else:
        print("Invalid Option!! please pick from these options %s"%validOptions)
        continue
print("Thank you for using Aingty's Binary Tree Program. Have a Wonderful rest of your day! :)")
