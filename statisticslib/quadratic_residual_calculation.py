import quadreg as quad
# This file takes a list of abscissae from the input of the dataset and performs quadratic regression on them,
# using the results to calculate residuals which it will then return as a list.
def residual_calculation(abscissae, ordinates):
    a, b, c = quad.quadreg(abscissae,ordinates)
    k = len(abscissae)
    observed = []
    predicted = []
    residual = []
    for i in range(0,k):
        observed.append(ordinates[i])
        predicted.append(a*pow(abscissae[i],2) + b*abscissae[i] + c)
        residual.append(observed[i] - predicted[i])
    return residual