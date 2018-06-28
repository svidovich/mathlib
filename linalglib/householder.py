# This is a QR Decomposition by householder reflectors. It takes as an argument
# a matrix A who has at least more rows than columns, and returns an upper triangular
# matrix R along with an orthogonal matrix Q.


# EXPERIMENTAL
# TODO: BUG TESTING
import numpy as np
import math

def householder(A,ordinates):
    shape = A.shape
    m = shape[0]
    n = shape[1]
    I = np.eye(m,n)
    v = np.zeros(shape=(n,1))
    Q = np.zeros(shape=(m,n))
    v = np.zeros(shape=(m,1))
    for k in range(0,n):
        x = A[k:m,k]
        v = x.reshape(m-k,1) + np.sign(x[0])*np.linalg.norm(x)*(I[k:m,k].reshape(m-k,1))
        v /= np.linalg.norm(v)
        A[k:m,k:n] = A[k:m,k:n] - 2*(v.dot((v.T.dot(A[k:m,k:n]))))
        n = len(ordinates)
        print(v)
    y = np.zeros(shape=(n,1))
    for i in range(0,n):
        y[i] = ordinates[i]
    u = y
    print(u)
    print(v)
    for k in range(0,n):
        print(k)
        u[k:m] -= 2*v.T.dot(v.T.dot(u[k:m]))
    R = A
    return u, R
