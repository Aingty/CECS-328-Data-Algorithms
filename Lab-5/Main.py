import random
import timeit
import sys

# Add Useful-Functions path for Window Machines below
sys.path.append('C:/Users/Aingty/Documents/GitHub Repositories/CECS-328-Data-Algorithms/Useful-Functions')
# Add Useful-Functions path for Mac Machines below
sys.path.append('')

from DecisionMaking import *
from TheHeaping import *

keepGoing = True
while keepGoing:
    avgHeapSortTime = 0
    n = input("\nPlease input the array size: ")
    repetition = input("How many repetition?: ")
    printing = input("Print array? y or Y: ")
    if repetition.isdigit() and n.isdigit():
        repetition = int(repetition)
        n = int(n)
        for j in range(repetition): 
            array1 = [0] * n
            for i in range(n):
                l = random.randint(-1000,1000)
                array1[i] = l
            if printing == "y" or printing == "Y":
                print("Generated Array: \n\t%s" %array1)
            start = timeit.default_timer()
            tempArray = heap_Sort(array1)
            end = timeit.default_timer()
            avgHeapSortTime += (end - start)
            print("Current runtime: %s"%avgHeapSortTime)
            if printing == "y" or printing == "Y":
                print("After Heap Sort: \n\t%s\n"%tempArray[::-1])
        print("Heap Sort Average Running Time: %s seconds"%(avgHeapSortTime/repetition))
        
        # Check to see if user wants to go again
        keepGoing = keepGoingDecision()
    else:
        print("Incorrect array size and/or repetition value!!")
    
