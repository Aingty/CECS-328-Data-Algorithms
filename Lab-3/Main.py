
import random
from Finding import *


keepGoing = True
while keepGoing:
    n = input("\nPlease input the array size: ")
    if n.isdigit():
        n = int(n)
        array = [0] * n
        for i in range(n):
            l = random.randint(-100,100)
            array[i] = l
        print("Generated Array: \n%s\n" %array)
        invalidK = True
        while invalidK:
            k = input("Please input a number from 1 to %.0f as k least element: " %n) 
            if k.isdigit():
                k = int(k)
                if k >= 1 and k <= n:
                    invalidK = False
                else:
                    print("Invalid K-value, please input within range!!")
            else:
                print("Invalid K-value, please input a number!!")
        print("The %.0fth least element in the array is %s" %(k,findingK(array,k)))
    else:
        print("Incorrect array size value!!!")
