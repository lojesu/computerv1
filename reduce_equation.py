"""
this function is isdigit but better
"""
def is_number(str):
    if str[0] == "-":
        str = str[1:]
    return str.isdigit()


"""
this function transfer tokens to the left equal to get "equation = 0"
"""
def transfer_all_token_to_the_left_equal(equation):
    left_equal = equation.split("=")[0]
    right_equal = equation.split("=")[1]
    right_equal_split = right_equal.split()
    new_right_equal = ""
    i = 0
    for token in right_equal_split:
        if i % 2 == 0:
            if i == 0:
                if is_number(token):
                    if int(token) * -1 >= 0:
                        new_right_equal += "+ " + str(int(token) * -1)
                    else:
                        new_right_equal += "- " + token
                else:
                    new_right_equal += token
            else:
                if token.isdigit() and \
                    (right_equal_split[i - 1] != "+" and \
                    right_equal_split[i - 1] != "-"):
                    new_right_equal += str(int(token) * -1)
                else:
                    new_right_equal += token
        elif i % 2 == 1:
            if token == "+":
                new_right_equal += "-"
            elif token == "-":
                new_right_equal += "+"
            else:
                new_right_equal += token
        i += 1
        new_right_equal += " "
    new_equation = left_equal + new_right_equal + "= 0"
    return new_equation


"""
this function reduce the equation for find the result more easily
"""
def reduce_equation(equation):
    if equation[equation.find("=") + 2] != "0":
        new_equation = transfer_all_token_to_the_left_equal(equation)
    return new_equation
