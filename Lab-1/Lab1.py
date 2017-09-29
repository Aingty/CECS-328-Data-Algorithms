#!/usr/bin/env Python

import random
from Search import *

# Prompting user for Array size
n = (int(input("Enter a positive number: ")))

array = [0] * n

for i in range(n):
    l = random.randint(-1001 , 1000)
    array[i] = l

array.sort()

# Picking a random existing number in array
for i in range(100):
    temp = random.randint(-1 , n-1)
    key = array[temp]

print(array)
