# TODO: Fix the algorithm so it's not a piece of shit

import numpy as np
def trig_interpolate(length,min,max):
    
    A0 = 0

    if  len(length) % 2 == 0:
        del length[0]
        N = len(length)
    else:
        N = len(length)
    # Determine the inputs
    x = np.zeros(N)
    for i in range (0,N):
        x[i] = ((np.pi)*(2*(i+1)))/(N)
    x = np.sort(x)
    # Determine the outputs
    y = np.zeros(N)
    for i in range(0,N):
        y[i] = np.sin(x[i])
    for i in range(0,N):
        A0 += (2/N)*y[i]

    M = int((N-1)/2)
    A = np.zeros(M)
    B = np.zeros(M)

    for h in range(0,M):
        for k in range(0,N):
            A[h] += ((2/N)*y[k]*(np.cos((2*(np.pi)*(h+1)*(k+1))/N)))
            B[h] += ((2/N)*y[k]*(np.sin((2*(np.pi)*(h+1)*(k+1))/N)))
    domain = np.arange(min,max+1,0.1)
    d = len(domain)
    psivalues = np.zeros(d)
    for i in range(0,d):
        psivalues[i] = A0/2
        for h in range(0,M):
            psivalues[i] += A[h]*np.cos((h+1)*domain[i]) + B[h]*np.sin((h+1)*domain[i])

    return domain,psivalues
