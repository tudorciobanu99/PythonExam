import numpy as np

def newtonrhapson(x0,n):
    if (n > 0 and x0 != 0):
        xs = np.zeros(n)
        xs[0] = x0 - (x0**3+x0**2)/(3*x0**2+2*x0)
        for i in range(1, n):
            xs[i] = xs[i-1] - (xs[i-1]**3+xs[i-1]**2)/(3*xs[i-1]**2+2*xs[i-1])
        x = xs[-1]
    else:
        x = x0
    return x