#!/usr/bin/env Python

import random
from Sorting import *


n = int(input("Please enter a positive number: "))

array = [0] * n

for i in range(n):
    l = random.randint(-7000 , 7000)
    array[i] = l

array = insertionSort(array)
print ("Insertion Sort: %s" %array)