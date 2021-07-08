from tools import (
    take_first,
    take_second,
    is_operator,
    )


"""
this function is isdigit but better
"""
def is_number(str):
    if str[0] == "-":
        str = str[1:]
    try:
        float(str)
        return True
    except:
        return False

"""
this function convert equation's number to tupple (number, power)
"""
def convert_equation_to_tupple(equation):
    new_equation = []
    equation_split = equation.split()
    i = 0
    while i < len(equation_split):
        token = equation_split[i]
        if is_number(token) == True and i < len(equation_split) - 2 and\
            equation_split[i + 1] == "*" and\
            equation_split[i + 2][0] == "X":
            new_equation.append((float(token), float(equation_split[i + 2][2:])))
            i += 2
        elif is_operator(token) == True:
            new_equation.append(token)
        elif is_number(token) == True:
            new_equation.append((float(token), 0))
        elif token[0] == "X":
            new_equation.append((1, float(token[2:])))
        else:
            break
        i += 1
    return new_equation


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
                elif token[0] == "X" or token[1] == "X":
                    if token[0] == "-":
                        new_right_equal += "+ "
                    else:
                        new_right_equal += "- "
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
this is the first step of final reduction of equation, i develope all * and /
"""
def reduction_first_step(equation):
    i = 0
    while i < len(equation) - 1:
        if equation[i] == "*":
            number = float(equation[i - 1][0] * equation[i + 1][0])
            power = float(equation[i - 1][1] + equation[i + 1][1])
            equation[i] = (number, power)
            del(equation[i - 1])
            del(equation[i])
            i = 0
        elif equation[i] == "/":
            try:
                number = float(equation[i - 1][0] / equation[i + 1][0])
            except:
                print("we get a division per zero, it makes no sense in mathematiques")
                quit()
            power = float(equation[i - 1][1] - equation[i + 1][1])
            equation[i] = (number, power)
            del(equation[i - 1])
            del(equation[i])
            i = 0
        i += 1
    return equation
                
"""
second step, i do + and - at token with the same power
"""
def reduction_second_step(equation):
    i = 0
    for token in equation:
        if type(token) == tuple:
            if take_first(token) == 0:
                equation[i] = (0, 0)
                i -= 1
        i += 1
    i = 0
    start = 0
    while start < len(equation) - 1:
        i = start + 2
        while take_second(equation[start]) != take_second(equation[i]):
            i += 2
            if i > len(equation) - 1:
                break
        if i <= len(equation) - 1:
            if equation[i - 1] == "+":
                new_number = float(take_first(equation[start])) + float(take_first(equation[i]))
                equation[start] = (new_number, take_second(equation[start]))
                del(equation[i])
                del(equation[i - 1])
            elif equation[i - 1] == "-":
                new_number = float(take_first(equation[start])) - float(take_first(equation[i]))
                equation[start] = (new_number, take_second(equation[start]))
                del(equation[i])
                del(equation[i - 1])
            start -= 2
        start += 2
    i = 0
    for token in equation:
        if take_first(token) == 0 and take_second(token) == 0:
            del(equation[i])
            del(equation[i])
        i += 1
    return equation


"""
this function reduce the equation for find the result more easily
"""
def reduce_equation(equation):
    if equation[equation.find("=") + 2] != "0":
        equation = transfer_all_token_to_the_left_equal(equation)
    new_equation = convert_equation_to_tupple(equation)
    new_equation = reduction_first_step(new_equation)
    new_equation = reduction_second_step(new_equation)
    return new_equation
