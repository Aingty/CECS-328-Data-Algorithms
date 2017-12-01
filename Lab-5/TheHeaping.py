
def build_MaxHeap(array):
    pass

def max_Heapify(array, root):
    maxIndex = root
    leftChild = 2*root
    rightChild = (2*root) + 1

    if leftChild <= len(array) and array[leftChild] > array[maxIndex]:
        maxIndex = leftChild
    if rightChild <= len(array) and array[rightChild] > array[maxIndex]:
        maxIndex = rightChild
    if maxIndex != root:
        array[maxIndex], array[root] = array[root], array[maxIndex]
    

def heap_Sort(array):
    return build_MaxHeap(array)