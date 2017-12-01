import random
import sys

# Add Useful-Functions path for Window Machines below
sys.path.append('C:/Users/Aingty/Documents/GitHub Repositories/CECS-328-Data-Algorithms/Useful-Functions')
# Add Useful-Functions path for Mac Machines below
sys.path.append('')


from DecisionMaking import *
from MSS import *

keepGoing = True
while keepGoing:
    n = input("\nPlease input the array size: ")
    if n.isdigit():
        n = int(n)
        # array1 = [-19,-7,-12,-4,-50,-5,-10,-2]
        # array1 = [19,-7,12,4,-50,5,10,-2]
        array1 = [0] * n
        for i in range(n):
            l = random.randint(-100,100)
            array1[i] = l
        print("Generated Array:\n\t%s"%array1)
        print("\nThe MSS using the fast method is %.0f\n" %fastMSS(array1))
        
        # Check to see if user wants to go again
        keepGoing = keepGoingDecision()
    else:
        print("Incorrect array size value!!")
        continue

