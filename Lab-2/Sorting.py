#!/usr/bin/env Python

import statistics

def insertionSort(array):
    swap = 1
    while swap != 0:
        swap = 0
        for i in range(len(array)):
            if(i+1 < len(array)):
                if(array[i] > array[i+1]):
                    array[i], array[i+1] = array[i+1], array[i]
                    swap = 1
    return array

def quickSort(array):
    # if statement for base case
    if(len(array) <= 3):
        return insertionSort(array)
    else:
        left = []
        right = []
        medianList = [array[0], array[(int)(len(array)/2)], array[len(array)-1]]
        pivot = statistics.median(medianList)
        for i in range(len(array)):
            if (array[i] <= pivot):
                left.append(array[i])
            else:
                right.append(array[i])
        left = quickSort(left)
        right = quickSort(right)
        return (left + right)        
            
