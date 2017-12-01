import random
import sys

# Add Useful-Functions path for Window Machines below
sys.path.append('C:/Users/Aingty/Documents/GitHub Repositories/CECS-328-Data-Algorithms/Useful-Functions')
# Add Useful-Functions path for Mac Machines below
sys.path.append('')

from DecisionMaking import *
from TheHeaping import *

keepGoing = True
while keepGoing:
    n = input("\nPlease input the array size: ")
    if n.isdigit():
        n = int(n)
        array1 = [0] * n
        for i in range(n):
            l = random.randint(-1000,1000)
            array1[i] = l

        print("Generated Array: \n%s\n" %array1)

        # Check to see if user wants to go again
        keepGoing = keepGoingDecision()
    else:
        print("Incorrect array size value!!!")
