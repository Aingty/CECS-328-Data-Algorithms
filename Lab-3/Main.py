
import random
import sys

# Add Useful-Functions path for Window Machines below
sys.path.append('C:/Users/Aingty/Documents/GitHub Repositories/CECS-328-Data-Algorithms/Useful-Functions')
# Add Useful-Functions path for Mac Machines below
sys.path.append('/Users/Aingty/Applications/GitHub Repositories/CECS-328-Data-Algorithms/Useful-Functions')

from DecisionMaking import *
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
        
        # Check to see if user wants to go again
        keepGoing = keepGoingDecision()
    else:
        print("Incorrect array size value!!!")
