
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

#def slowMSS(array):
