# This is a linear regression algorithm. It will generate a and b as floats in y = a + bx.
# The arguments need to be lists, abscissae first, then ordinates.

import numpy as np
import sys

def linreg(abscissae, ordinates):
    if len(abscissae) != len(ordinates):
        print("Sample mismatch. You have " + str(len(abscissae)) + " abscissae, and " + str(len(ordinates)) + " ordinates.\n")
        print("These numbers should be the same.\n")
        exit(1)
    n = len(abscissae)
    
    ordinates = list(map(int, ordinates))
    abscissae = list(map(int, abscissae))

    sumx = 0
    for element in abscissae:
       sumx += element
    sumy = 0
    for element in ordinates:
        sumy += element
    xbar = (1/n)*sumx
    ybar = (1/n)*sumy

    beta_numerator = 0
    for i in range(0,n):
        beta_numerator += (abscissae[i] - xbar)*(ordinates[i] - ybar)
    beta_denominator = 0
    for i in range(0,n):
        beta_denominator += pow((abscissae[i]-xbar),2)
    b = beta_numerator/beta_denominator
    a = ybar - b*xbar

    return a, b
