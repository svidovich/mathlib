import numpy as np
import matplotlib
def trig_interpolate(ordinates):
    
    A0 = 0

    if  len(ordinates) % 2 == 0:
        del ordinates[0]
        N = len(ordinates)
        print(N)
    else:
        N = len(ordinates)
    print(N)
    # Determine the inputs
    x = np.zeros(N)
    for i in range (0,N):
        x[i] = ((np.pi)*(2*i))/N
    x = np.sort(x)
    # Determine the outputs
    y = np.zeros(N)
    for i in range(0,N):
        y[i] = ordinates[i]
    for i in range(0,N):
        A0 += (2/N)*y[i]

    M = int((N-1)/2)
    A = np.zeros(M)
    B = np.zeros(M)

    for h in range(0,M-1):
        for k in range(0,N-1):
            A[h] += ((2/N)*y[k]*(np.cos((2*(np.pi)*h*k)/N)))
            B[h] += ((2/N)*y[k]*(np.sin((2*(np.pi)*h*k)/N)))
    domain = np.arange(0,90,0.1)
    d = len(domain)
    psivalues = np.zeros(d)
    for i in range(0,d-1):
        psivalues[i] = A0/2
        for h in range(0,M-1):
            psivalues[i] += A[h]*np.cos(h*domain[i]) + B[h]*np.cos(h*domain[i])
    for i in range(len(domain)):
        print("(" + str(domain[i]) + ", " + str(psivalues[i]) + ")")
    return domain,psivalues
