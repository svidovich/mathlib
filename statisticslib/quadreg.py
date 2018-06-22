# ax2 + bx + c
# TODO: Fix this fucking mess

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
    
    

    a_numerator = ((sum_on_x2y - (1/n)*sum_on_x2_sum_on_y)*(sum_on_squared_xs - (1/n)*pow(sum_on_xs,2))) - ((sum_on_xy - (1/n)*sum_on_x_sum_on_y)*(sum_on_cubed_xs - (1/n)*sum_on_xs*sum_on_squared_xs))
    a_denominator = ((sum_on_squared_xs - (1/n)*pow(sum_on_xs,2)))*(sum_on_tetra_xs - (1/n)*pow(sum_on_squared_xs,2)) - pow(sum_on_cubed_xs - (1/n)*sum_on_xs*sum_on_squared_xs,2)

    a = a_numerator/a_denominator

    b_numerator = ((sum_on_xy - (1/n)*sum_on_x_sum_on_y)*(sum_on_tetra_xs - (1/n)*pow(sum_on_squared_xs,2))) - ((sum_on_x2y - (1/n)*pow(sum_on_xs,2)*(sum_on_cubed_xs - (1/n)*sum_on_squared_xs*sum_on_xs)))
    b_denominator = ((sum_on_squared_xs - (1/n)*pow(sum_on_xs,2))*(sum_on_tetra_xs - (1/n)*pow(sum_on_squared_xs,2))) - pow(sum_on_tetra_xs - (1/n)*sum_on_squared_xs,2)

    b = b_numerator/b_denominator

    c = (1/n)*sum_on_ys - ((b/n)*sum_on_xs - (a/n)*sum_on_squared_xs)

    
    return a, b, c
