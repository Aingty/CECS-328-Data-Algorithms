
def build_MaxHeap(array):
    for i in range(len(array)-1, -1, -1):
        max_Heapify(array, i)


def max_Heapify(array, root):
    maxIndex = root
    leftChild = (2*root) + 1
    rightChild = (2*root) + 2

    if leftChild <= len(array)-1:
        if array[leftChild] > array[maxIndex]:
            maxIndex = leftChild
    if rightChild <= len(array)-1:
        if array[rightChild] > array[maxIndex]:
            maxIndex = rightChild
    if maxIndex != root:
        array[maxIndex], array[root] = array[root], array[maxIndex]
    

def heap_Sort(array):
    tempArray = []
    for i in range(len(array)):
        build_MaxHeap(array)
        array[0], array[len(array)-1] = array[len(array)-1], array[0]
        tempArray.append(array.pop())
    return tempArray