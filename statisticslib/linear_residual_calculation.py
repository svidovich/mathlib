import linreg as lin
# This file takes a list of abscissae from the input of the dataset and performs linear regression on them,
# using the results to calculate residuals which it will then return as a list.
def residual_calculation(abscissae, ordinates):
    a, b = lin.linreg(abscissae,ordinates)
    k = len(abscissae)
    observed = []
    predicted = []
    residual = []
    for i in range(0,k):
        observed.append(ordinates[i])
        predicted.append(a + b*abscissae[i])
        residual.append(observed[i] - predicted[i])
    return residual