#!/usr/bin/env Python

import random
import sys
import platform
from Sorting import *

#print(platform.architecture())
n = int(input("\nPlease enter a positive number: "))

array1 = [0] * n
array2 = [0] * n
for i in range(n):
    l = random.randint(-7000 , 7000)
    array1[i] = l
    array2[i] = l

insertionSort(array1)
print ("\nInsertion Sort: %s \n" %array1)

# array2 = quickSort(array2)
# print("Quick sort: %s \n" %array2)

quickSortIterative(array2, 0, len(array2)-1)    
print ("Quick Sort: %s \n" %array2)