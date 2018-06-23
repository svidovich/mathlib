# This function takes a matching list of abscissae and ordinates and performs quadratic regression on them, returning
# the coefficients of the regression polynomial ax^2 + bx + c


from math import pow

def quadreg(abscissae, ordinates):
    if len(abscissae) != len(ordinates):
        print("Sample mismatch. You have " + str(len(abscissae)) + " abscissae, and " + str(len(ordinates)) + " ordinates.\n")
        print("These numbers should be the same.\n")
        exit(1)

    n = len(abscissae)

    ordinates = list(map(int, ordinates))
    abscissae = list(map(int, abscissae))

    sum_on_xs = 0
    for i in range(0,n):
        sum_on_xs += abscissae[i]
    
    sum_on_ys = 0
    for i in range(0,n): 
        sum_on_ys += ordinates[i]
    
    sum_on_squared_xs = 0
    for i in range(0,n):
        sum_on_squared_xs += pow(abscissae[i],2)
    
    sum_on_cubed_xs = 0
    for i in range(0,n):
        sum_on_cubed_xs += pow(abscissae[i],3)
    
    sum_on_tetra_xs = 0
    for i in range(0,n):
        sum_on_tetra_xs += pow(abscissae[i],4)
    
    sum_on_xy = 0
    for i in range(0,n):
        sum_on_xy += abscissae[i]*ordinates[i]
    
    sum_on_x_sum_on_y = 0
    for i in range(0,n):
        sum_on_x_sum_on_y += sum_on_xs*sum_on_ys

    sum_on_x2y = 0
    for i in range(0,n):
        sum_on_x2y += pow(abscissae[i],2)*ordinates[i]
    
    sum_on_x2_sum_on_y = 0
    for i in range(0,n):
        sum_on_x2_sum_on_y += sum_on_squared_xs*sum_on_ys
    
    S11 = sum_on_squared_xs - (1/n)*pow(sum_on_xs,2)    
    S12 = sum_on_cubed_xs - (1/n)*sum_on_xs*sum_on_squared_xs
    S22 = sum_on_tetra_xs - (1/n)*pow(sum_on_squared_xs,2)
    Sy1 = sum_on_xy - (1/n)*sum_on_ys*sum_on_xs
    Sy2 = sum_on_x2y - (1/n)*sum_on_ys*sum_on_squared_xs

    xbar = (1/n)*sum_on_xs
    x2bar = (1/n)*sum_on_squared_xs
    ybar = (1/n)*sum_on_ys

    b = (Sy1*S22 - Sy2*S12)/(S22*S11 - pow(S12,2))
    a = (Sy2*S11 - Sy1*S12)/(S22*S11 - pow(S12,2))
    c = ybar - b*xbar - a*x2bar
    
    return a, b, c
