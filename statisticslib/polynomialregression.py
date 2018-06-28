import sys
sys.path.append('..')
from mathlib.linalglib.regression_vandermonde import * 
from mathlib.linalglib.backsub import *
from mathlib.linalglib.householder import *
import numpy as np

def polynomialregression(abscissae, ordinates, degree):
    A = vander(abscissae,degree)
    qty,R = householder(A,ordinates)
    n = len(ordinates)
    y = np.zeros(shape=(n,1))
    for i in range(0,n):
        y[i] = ordinates[i]
    b = backsub(R,qty)
    print(A)
    print(y)
    print(b)