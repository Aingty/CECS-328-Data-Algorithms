#!/usr/bin/env Python

import random
import sys
import timeit
from Sorting import *
sys.setrecursionlimit(150000)


n = int(input("\nPlease enter a positive number: "))

array = [0] * n

insertionTime = 0
quickTime = 0
for i in range(n):
    l = random.randint(-7000 , 7000)
    array[i] = l


array1 = insertionSort(array)

print("\nThe array: %s" %array1)


# for i in range(100):
    
#     start = timeit.default_timer()
#     array1 = insertionSort(array)
#     end = timeit.default_timer()
#     insertionTime = insertionTime + (end - start)
    
#     start = timeit.default_timer()
#     array2 = quickSort(array)
#     end = timeit.default_timer()
#     quickTime = quickTime + (end - start)

# insertionTime = insertionTime/100
# quickTime = quickTime/100

# print ("\nAverage Insertion Sort Time: %f \n" %insertionTime)
# print ("Average Quick Sort Time: %f \n" %quickTime)