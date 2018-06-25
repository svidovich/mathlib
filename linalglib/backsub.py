# This function will solve an upper triangular system Ux = b by back-substitution input matrix U.
# Input matrix U is an n by n upper triangular matrix
import numpy as np
import sys

def backsub(U,b):
    size = np.shape(U)
    n = size[0]
    x = np.zeros(shape=(n,1))
    for i in range(n-1,-1,-1):
        if U[i,i] == 0:
            print("Matrix is singular...")
            sys.exit(1)
        x[i] = b[i]/U[i,i]
        for j in range(0,i):
            b[j] = b[j] - U[j,i]*x[i]
    return x