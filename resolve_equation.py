from parsing import is_operator


"""
this function assign a, b and c values for apply the formules lower
"""
def assign_values(equation):
    i = 0
    new_equation = []
    for token in equation:
        if token == "-":
            equation[i + 1] = (equation[i + 1][0] * -1, equation[i + 1][1])
        if is_operator(token) == False:
            new_equation.append(token)
        i += 1
    a = 0
    b = 0
    c = 0
    for token in new_equation:
        if token[1] == 0:
            c = token[0]
        if token[1] == 1:
            b = token[0]
        if token[1] == 2:
            a = token[0]
    return a, b, c


"""
we just parse request user and we answer correctly
"""
def resolve_degree_0(equation, equation_parsing):
    a, b, c = assign_values(equation)
    if c == 0 and equation_parsing.count("X") > 0:
        print("All real number is a solution for this equation")
    elif c == 0 and equation_parsing.count("X") == 0:
        print("Your equality is true")
    elif c != 0 and equation_parsing.count("X") > 0:
        print("Your equation is unsolvable with real number")
    else:
        print("Your equality is FALSE !!")


"""
we isolate the X unknow and we split his factor to get a result
"""
def resolve_degree_1(equation):
    a, b, c = assign_values(equation)
    solution = -1 * c / b
    print("Solution is :", solution)


"""
we apply stupidly the formules and calculate solution(s)
"""
def resolve_degree_2(equation):
    a, b, c = assign_values(equation)
    delta = float(-4 * a * c)
    print("Delta is :", delta)
    if delta < 0:
        print("po trouve")
    elif delta == 0:
        solution = -b / (2 * a)
        print("Solution is :", solution)
    else:
        s1 = (-b - delta ** 0.5) / 2
        s2 = (-b + delta ** 0.5) / 2
        print("The two solutions are :", s1, "and", s2)