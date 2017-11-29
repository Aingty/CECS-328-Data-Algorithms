#!/usr/bin/env Python

import random
import sys
import platform
import timeit

from Sorting import *

#print(platform.architecture())
n = int(input("\nPlease enter an array size: "))
m = int(input("How many repetition? : "))
array1 = [0] * n
array2 = [0] * n

insertionSum = 0
quickSum = 0
for i in range(m):
    for i in range(n):
        l = random.randint(-7000 , 7000)
        array1[i] = l
        array2[i] = l
    start = timeit.default_timer()
    insertionSort(array1)
    end = timeit.default_timer()
    insertionSum+=(end - start)
    # Recursive Sorting:
    # array2 = quickSort(array2)
    # print("Quick sort: %s \n" %array2)
    start = timeit.default_timer()
    quickSortIterative(array2, 0, len(array2)-1)    
    end = timeit.default_timer()
    quickSum+=(end-start)
print("Insertion Sort Running Time: %s seconds" %(insertionSum/m))
print("Quick Sort Running Time: %s seconds" %(quickSum/m))

# print ("\nInsertion Sort: %s \n" %array1)
# print ("Quick Sort: %s \n" %array2)
