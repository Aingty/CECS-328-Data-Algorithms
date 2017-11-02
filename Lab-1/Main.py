#!/usr/bin/env Python

import random
import timeit
import math
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



ToMicrosecond = 1000000
ToMilisecond = 1000
ToSecond = 10000000
# Printing out the loop time
print "\n********************* Part A *********************"
print "Average Linear Search Time: %.2f milisecond" %(round((bothLinearTime/500)*ToMilisecond, 2))
print "Average Binary Search Time: %.2f microsecond" %(round((bothBinaryTime/500)*ToMicrosecond, 2))


# Calculating the timer to find non-existing number
key = 5000

start = timeit.default_timer()
linearSearch(array, key)
end = timeit.default_timer()
linearTime = end - start

linearTime = (linearTime/n)

start = timeit.default_timer()
binarySearch(array, key)
end = timeit.default_timer()
binaryTime = end - start

binaryTime = (binaryTime/(math.log(n,2)))

print "\n\n********************* Part B *********************"
# Printing out all Time for searches
print "One-Line Time of Linear Search for n = %d : %.2f milisecond" %(n, round((linearTime)*ToMicrosecond, 2))
print "One-Line Time of Binary Search for n = %d : %.2f microsecond\n" %(n, round((binaryTime)*ToMicrosecond, 2))

print "Estimate Time of Linear Search for n = 10^7 : %.2f second" %(linearTime*ToSecond)
print "Estimate Time of Binary Search for n = 10^7 : %f second" %(binaryTime*(math.log(ToSecond,2)))