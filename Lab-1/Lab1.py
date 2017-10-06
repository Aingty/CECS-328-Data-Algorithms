#!/usr/bin/env Python

import random
import timeit
from Search import *

# Prompting user for Array size
n = (int(input("\nEnter a positive number: ")))

# Variables for logging search time
bothTime = 0

array = [0] * n

for i in range(n):
    l = random.randint(-1001 , 1000)
    array[i] = l

array.sort()

# Calculating the timer to find exisitng number
start = timeit.default_timer()
for i in range(500):
    temp = random.randint(-1 , n-1)
    key = array[temp]
    linearSearch(array, key)
    binarySearch(array, key)

end = timeit.default_timer()

bothTime = (end - start)

# Printing out the loop time
print "\nExisting Search Time"
print "Average Search Time: %.2f milisecond" %(round((bothTime/500)*1000, 2))

# Calculating the timer to find non-existing number
key = 5000

linearSearch(array, key)
start = timeit.default_timer()
binarySearch(array, key)
end = timeit.default_timer()

bothTime = (end - start)

print "\n\nNon-Existing Search Time"
# Printing out all Time for searches
print "One Step Time for n=%.0f : %.2f microsecond" %(n,round((bothTime)*1000000, 2))
print "Estimate Time for n=10^7 : %.2f second" %(bothTime*10000000)