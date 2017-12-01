import random
from MSS import *

keepGoing = True
while keepGoing:
    n = input("\nPlease input the array size: ")
    if n.isdigit():
        n = int(n)
        # array1 = [-19,-7,-12,-4,-50,-5,-10,-2]
        # array1 = [19,-7,12,4,-50,5,10,-2]
        array1 = [0] * n
        for i in range(n):
            l = random.randint(-100,100)
            array1[i] = l
    else:
        print("Incorrect array size value!!")
        continue

    print("Generated Array:\n\t%s"%array1)
    print("\nThe MSS using the fast method is %.0f\n" %fastMSS(array1))
