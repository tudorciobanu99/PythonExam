import numpy as np

def hindex(c):
    passedCitations = 0
    c = np.sort(c)
    c = c[::-1]
    for i in range(len(c)):
        if (c[i] >= i+1):
            passedCitations += 1
    h = passedCitations
    return h