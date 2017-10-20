#!/usr/bin/env Python

import random
import timeit
from Search import *

# Prompting user for Array size
n = (int(input("\nEnter a positive number: ")))

# Variables for logging search time
bothLinearTime = 0
bothBinaryTime = 0

array = [0] * n

for i in range(n):
    l = random.randint(-1001 , 1000)
    array[i] = l

array.sort()

# Calculating the timer to find exisitng number
for i in range(500):
    temp = random.randint(-1 , n-1)
    key = array[temp]

    linearStartTime = timeit.default_timer()
    linearSearch(array, key)
    linearEndTime = timeit.default_timer()
    bothLinearTime = bothLinearTime + (linearEndTime - linearStartTime)

    binaryStartTime = timeit.default_timer()
    binarySearch(array, key)
    binaryEndTime = timeit.default_timer()
    bothBinaryTime = bothBinaryTime + (binaryEndTime - binaryStartTime)



convertToMicrosecond = 1000000
convertToMilisecond = 1000
# Printing out the loop time
print "\n********************* Part A *********************"
print "Average Linear Search Time: %.2f milisecond" %(round((bothLinearTime/500)*1000, 2))
print "Average Binary Search Time: %.2f microsecond" %(round((bothBinaryTime/500)*convertToMicrosecond, 2))


# Calculating the timer to find non-existing number
key = 5000


linearSearch(array, key)


start = timeit.default_timer()
binarySearch(array, key)
end = timeit.default_timer()

bothTime = (end - start)

print "\n\n********************* Part B *********************"
# Printing out all Time for searches
print "One Step Time for n=%.0f : %.2f microsecond" %(n,round((bothTime)*convertToMicrosecond, 2))
print "Estimate Time for n=10^7 : %.2f second\n" %(bothTime*10000000)