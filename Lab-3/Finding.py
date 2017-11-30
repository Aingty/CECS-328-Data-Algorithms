# Function to find the kth least element

def findingK(array, k):
    # First element to be pivot
    tempArray = array
    left = []
    right = []
    kNotFound = True
    while kNotFound:
        pivot = tempArray[0]
        for i in range(len(tempArray)):
            if i == 0:
                continue
            if(tempArray[i] <= pivot):
                left.append(tempArray[i])
            else:
                right.append(tempArray[i])
        print(left,right)
        left.append(pivot)
        tempArray = []
        # Check if K-value is left or right
        if k < len(left):
            tempArray = left
        elif k > len(left):
            k = k - len(left)
            tempArray = right
        else:
            return pivot
