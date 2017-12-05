import random
import timeit
import sys

# Add Useful-Functions path for Window Machines below
sys.path.append('C:/Users/Aingty/Documents/GitHub Repositories/CECS-328-Data-Algorithms/Useful-Functions')
# Add Useful-Functions path for Mac Machines below
sys.path.append('/Users/Aingty/Applications/GitHub Repositories/CECS-328-Data-Algorithms/Useful-Functions')

from DecisionMaking import *
from TheHeaping import *
from Sorting import *

keepGoing = True
while keepGoing:
    avgHeapSortTime = 0
    avgSelectionSortTime = 0
    avgQuickSortTime = 0
    n = input("\nPlease input the array size: ")
    repetition = input("How many repetition?: ")
    printing = input("Print array? (Y or y): ")
    comparison = input("Compare to which sort:\t1. Selection\t2. Quick\n\tYour Choice: ")
    if comparison.isdigit():
        comparison = int(comparison)
    else:
        print("Not comparing to any sort.....")
    if repetition.isdigit() and n.isdigit():
        repetition = int(repetition)
        n = int(n)
        for j in range(repetition): 
            array1 = [0] * n
            array2 = [0] * n
            for i in range(n):
                l = random.randint(-1000,1000)
                array1[i] = l
                array2[i] = l
            # Print the array if chosen by user
            if printing == "y" or printing == "Y":
                print("\nGenerated Array: \n\t%s\n" %array1)

            start = timeit.default_timer()
            tempArray = heap_Sort(array1)
            end = timeit.default_timer()
            avgHeapSortTime += (end - start)
            print("Current runtime HeapSort: %s seconds"%avgHeapSortTime)

            # Sorting using selection if chosen by user
            if comparison == 1:
                start = timeit.default_timer()
                selectionSort(array2)
                end = timeit.default_timer()
                avgSelectionSortTime += (end - start)
                print("Current runtime SelectionSort: %s seconds\n"%avgSelectionSortTime)
                # Print the sorted array if chosen by user
                if printing == "y" or printing == "Y":
                    print("After Selection Sort: \n\t%s\n"%array2[::-1])
            
            # Sorting using quick sort if chosen by user
            if comparison == 2:
                start = timeit.default_timer()
                quickSortIterative(array2, 0, len(array2)-1)    
                end = timeit.default_timer()
                avgQuickSortTime += (end - start)
                print("Current runtime QuickSort: %s seconds\n"%avgQuickSortTime)
                # Print the sorted array if chosen by user
                if printing == "y" or printing == "Y":
                    print("After Quick Sort: \n\t%s\n"%array2)


            # Print the sorted array if chosen by user
            if printing == "y" or printing == "Y":
                print("After Heap Sort: \n\t%s\n"%tempArray[::-1])
        
        print("Heap Sort Average Running Time: %s seconds"%(avgHeapSortTime/repetition))
       
        # Print the selection average runtime if chosen by user
        if comparison == 1:
            print("Selection Sort Average Running Time: %s seconds"%(avgSelectionSortTime/repetition))

        if comparison == 2:
            print("Quick Sort Average Running Time: %s seconds"%(avgQuickSortTime/repetition))
        print("\n")
        
        # Check to see if user wants to go again
        keepGoing = keepGoingDecision()
    else:
        print("Incorrect array size and/or repetition value!!")
    
