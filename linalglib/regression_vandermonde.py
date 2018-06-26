# This function takes in a set of inputs and a degree and constructs the approprate
# vandermonde matrix for a regression algorithm with a given degree.
# WARNING: THIS CAN BE USED FOR INTERPOLATION BY THE WISE. CHOOSE degree CAREFULLY


# EXPERIMENTAL
# TODO: BUG TESTING
import numpy as np
from math import pow

def vander(abscissae,degree):
    n = len(abscissae)
    V = np.zeros(shape=(n,degree))
    for i in range(0,n):
        for j in range(0,degree):
            V[i,j] = pow(abscissae[i],j)
    return V