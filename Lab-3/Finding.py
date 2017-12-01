# Function to find the kth least element

def findingK(array, k):
    # First element to be pivot
    tempArray = array
    kNotFound = True
    while kNotFound:
        left = []
        right = []
        pivot = tempArray[0]
        for i in range(len(tempArray)):
            if i == 0:
                continue
            if(tempArray[i] <= pivot):
                left.append(tempArray[i])
            else:
                right.append(tempArray[i])
        left.append(pivot)
        tempArray = []
        # Check if K-value is left or right
        if k < len(left) and k != 0:
            tempArray = left
        elif k > len(left) and k != 0:
            k = k - len(left)
            tempArray = right
        else:
            kNotFound = False
            return pivot
