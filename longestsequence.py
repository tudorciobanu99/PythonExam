import numpy as np

def longestsequence(s):
    if (len(s) > 0):
        prev = s[0]
        l = 1
    counter = np.array([], dtype = int)
    for i in range(1,len(s)):
        if (s[i] == prev):
            l += 1
            if (i == len(s) - 1):
                counter = np.append(counter, l)
        else:
            counter = np.append(counter,l)
            l = 1
        prev = s[i]
    if (len(counter) > 0):
        l = np.max(counter)
    elif (len(s) == 0):
        l = 0
    else:
        l = 1
    return l