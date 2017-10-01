#!/usr/bin/env Python

def linearSearch(array, key):
    n = len(array)
    for i in range(n):
        if key == array[i]:
            return True
    return False

def binarySearch(array, key):
    start = 0
    end = len(array) - 1
    while(start <= end):
        mid = int((start + end)/2)
        if(key==array[mid]):
            return True
        elif (key > array[mid]):
                start = mid + 1
        else:
            end = mid - 1
    return False