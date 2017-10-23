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
        swap = 0
        while swap != 0:
            swap = 0    
            for i in range(len(array)):
                if(i+1 < len(array)):
                    if(array[i] > array[i+1]):
                        array[i], array[i+1] = array[i+1], array[i]
                        swap = 1
            
            
    medianList = [array[0], array[len(array)/2], array[len(array)]]
    statistics.median(medianList)
