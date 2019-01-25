import numpy as np

def ctsummary(T):
    sunsorted = np.array([])
    currency = [0.5,1,2,5,10,20]
    for i in range(np.size(T,0)):
        currentSum = 0
        for j in range(np.size(T,1)):
            currentSum += T[i,j] * currency[j]
        sunsorted = np.append(sunsorted, currentSum)
    s = np.sort(sunsorted)
    s = s[::-1]
    return s