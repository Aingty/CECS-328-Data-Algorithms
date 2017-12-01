
import random
from Finding import *


keepGoing = True
while keepGoing:
    n = input("\nPlease input the array size: ")
    if n.isdigit():
        n = int(n)
        array1 = [0] * n
        array2 = [0] * n
        for i in range(n):
            l = random.randint(-100,100)
            array1[i] = l
            array2[i] = l
        print("\nGenerated Array: \n%s\n" %array1)
        print("Sorted: \n%s\n" %sorted(array2))
        invalidK = True
        while invalidK:
            k = input("Please input a number from 1 to %.0f as k least element: " %n) 
            if k.isdigit():
                k = int(k)
                if k >= 1 and k <= n:
                    invalidK = False
                else:
                    print("Invalid K-value, please input within range!!")
            else:
                print("Invalid K-value, please input a number!!")
        print("The %.0fth least element in the array is %s" %(k,findingK(array1,k)))
        invalidDecision = True
        while invalidDecision:
            decision = input("\nGo again? Y or N\n\tYour Choice: ")
            if decision=='y' or decision=='Y':
                invalidDecision = False
                continue
            elif decision=='n' or decision=='N':
                invalidDecision = False
                keepGoing = False
            else:
                print("Sorry invalid input!!")
    else:
        print("Incorrect array size value!!!")
