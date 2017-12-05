#!/usr/bin/env Python

import statistics


def insertionSort(array):
    """
    Find the highest values and move it to the last indexes
    """
    swap = 1
    while swap != 0:
        swap = 0
        for i in range(len(array)):
            if(i+1 < len(array)):
                if(array[i] > array[i+1]):
                    array[i], array[i+1] = array[i+1], array[i]
                    swap = 1
    return array          

def selectionSort(array):
    """
    Find the lowest values and move it to the last indexes
    """
    noSwap = True
    while noSwap:
        noSwap = False
        for i in range(len(array)):
            if(i+1 < len(array)):
                if(array[i+1] > array[i]):
                    array[i+1], array[i] = array[i], array[i+1]   
                    noSwap = True
    return array

def quickSort(array):
    """
    Recursive quick sort: Divide array until size is less than 4 and then call insertion sort on it. Then combine array into one.
    """
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

def spliter(array, left, right):
    """
    Function used to spit the array into two and swap with pivot
    """
    pivot = array[left]
    first = left + 1
    last = right
    while True:
        while first <= last and array[first] <= pivot:
            first+=1
        while last >= first and array[last] >= pivot:
            last-=1
        if last <= first:
            break
        # Swapping according to pivot
        array[first], array[last] = array[last], array[first]
    array[left], array[last] = array[last], array[left]
    return last

def quickSortIterative(array, left, right):
    """
    Interative quick sort: Divide array then call spitter function till the array is sorted
    """
    stack = []
    stack.append((left,right))
    while stack:
        position = stack.pop()
        left = position[0]
        right = position[1]
        pivot = spliter(array, left, right)
        if pivot - 1 > left:
            stack.append((left, pivot - 1))
        if pivot + 1 < right:
            stack.append((pivot + 1, right))