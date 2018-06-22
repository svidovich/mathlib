# This t distribution algorithm takes in a sample size and spits out values of a t distribution.

import math
import sys

def tstudent(sample_size, datapoints):
        pi = 3.141592653589
        if sample_size % 2 == 0:
            print("This algorithm doesn't integrate. It uses factorials. Because of this, you're going to need\n")
            print("to have an odd sample size.")
            exit(1)
        
        coefficient_numerator = math.factorial((sample_size - 2)/2)
        coefficient_denominator = math.sqrt(sample_size*pi)
        coefficient = coefficient_numerator/coefficient_denominator
        values = []

    return