# This is a QR Decomposition by householder reflectors. It takes as an argument
# a matrix A who has at least more rows than columns, and returns an upper triangular
# matrix R along with an orthogonal matrix Q.


# EXPERIMENTAL
# TODO: BUG TESTING
import numpy as np


def householder(A):
    shape = A.shape
    m = shape[0]
    n = shape[1]
    I = np.eye(m,n)
    v = np.zeros(n,1)
    Q = np.zeros(m,n)
    for k in range(0,n):
        x = np.zeros(m-k,1)
        for i in range(0,m-k):
            x[i,0] = A[i + k,k]
        v[k] = x + np.sign(x[0])*np.linalg.norm(x)*e[:,1]
        v[k] /= np.linalg.norm(v[k])
        A[k:m,k:n] -= 2*(v*(v.T))*A[k:m,k:n]
        Q[k:m,k] = v
    R = A
    return Q, R
