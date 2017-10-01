#!/usr/bin/env Python

import random
import timeit
from Search import *

# Prompting user for Array size
n = (int(input("\nEnter a positive number: ")))

# Variables for logging search time
linearTime = 0
binaryTime = 0
bothTime = 0

array = [0] * n

for i in range(n):
    l = random.randint(-1001 , 1000)
    array[i] = l

array.sort()

# Calculating the timer to find exisitng number
for i in range(500):
    temp = random.randint(-1 , n-1)
    key = array[temp]
    
    start = timeit.default_timer()
    linearSearch(array, key)
    end = timeit.default_timer()
    linearTime += (end - start)
    
    start = timeit.default_timer()
    binarySearch(array, key)
    end = timeit.default_timer()
    binaryTime += (end - start)

    bothTime += (linearTime + binaryTime)

# Printing out all Time for searches
print "Linear Search Time: %.2f microsecond" %(round((linearTime/500)*100000,2));
print "Binary Search Time: %.2f microsecond" %(round((binaryTime/500)*100000, 2))
print "Both Search Time: %.2f microsecond" %(round((bothTime/500)*100000, 2))