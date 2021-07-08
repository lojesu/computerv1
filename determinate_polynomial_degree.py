from reduce_equation import take_second


def determinate_polynomial_degree(equation):
    polynomial_degree = 0
    for token in equation:
        if type(token) == tuple:
            if take_second(token) < 0:
                print("we can't resolve an equation with a negative power")
                quit()
            if take_second(token) > polynomial_degree:
                polynomial_degree = take_second(token)
    if polynomial_degree > 2:
                print("we can't resolve equation with a power greater than 2")
                quit()
    return polynomial_degree
