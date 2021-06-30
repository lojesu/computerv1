from reduce_equation import take_second


def determinate_polynomial_degree(equation):
    polynomial_degree = 0
    for token in equation:
        if type(token) == tuple:
            if take_second(token) < 0:
                print("AHHHHHHHH !!!")
                quit()
            if take_second(token) > polynomial_degree:
                polynomial_degree = take_second(token)
    return polynomial_degree
