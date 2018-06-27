import sys
sys.path.append('..')
from mathlib.linalglib.regression_vandermonde import * 
from mathlib.linalglib.backsub import *
from mathlib.linalglib.householder import *
import numpy as np

def polynomialregression(abscissae, ordinates, degree):
    A = vander(abscissae,degree)
    Q,R = householder(A)
    n = len(ordinates)
    y = np.zeros(shape=(n,1))
    for i in range(0,n):
        y[i] = ordinates[i]
    v = Q.T*y
    b = backsub(R,v)
    print(b)