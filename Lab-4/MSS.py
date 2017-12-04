
def fastMSS(array):
    temp = 0
    mss = array[0]
    for i in range(len(array)):
        temp += array[i]
        if mss < temp:
            mss = temp
        if temp < 0:
            temp = 0
    return mss

def slowMSS(array):
    if len(array) < 2:
        return fastMSS(array)
    else:
        left = []
        right = []
        middle = int(len(array)/2)
        for i in range(middle):
            left.append(array[i])
        for i in range(middle, len(array)):
            right.append(array[i])
        return max(slowMSS(left), slowMSS(right), fastMSS(left+right))