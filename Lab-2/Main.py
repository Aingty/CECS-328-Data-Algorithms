#!/usr/bin/env Python

import random
import sys
from Sorting import *


n = int(input("\nPlease enter a positive number: "))

array = [0] * n

for i in range(n):
    l = random.randint(-7000 , 7000)
    array[i] = l

sys.setrecursionlimit(1500)


array1 = insertionSort(array)
print ("\nInsertion Sort: %s \n" %array)

array2 = quickSort(array)
print ("Quick Sort: %s \n" %array)