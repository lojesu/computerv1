"""
function for determinate if the tokken is an operator
"""
def is_operator(token):
    if token == "+" or token == "-" or token =="*" or token == "/" or token == "^":
        return True
    return False
    

"""
function for define the precedence value of operator
"""
def precedence_value(operator):
    if operator == "+" or operator == "-":
        return 2
    elif operator == "*" or operator == "/":
        return 3
    elif operator == "^":
        return 4
    return 0


"""
function for define the right operators's associativity
"""
def right_associativity(operator):
    if operator == "^":
        return "right"
    return "left"


"""
shunting-yard algo application, this is for convert in "reverse polish"
"""
def shunting_yard(calcul):
    output = ""
    operator_stack = ""

    for token in calcul.split():
        if token.isdigit():
            output += token + " "
        elif is_operator(token):
            for operator in operator_stack[::-1]:
                if operator == "(":
                    break
                if (precedence_value(token) <= precedence_value(operator) \
                    and right_associativity(token) == "left") \
                    or (right_associativity(token) == "right" \
                    and precedence_value(token) < precedence_value(operator)):
                    output += operator + " "
                    operator_stack = operator_stack[:-1]
            operator_stack += token
        elif token == "(":
            operator_stack += token
        elif token == ")":
            if "(" not in operator_stack:
                print("there are mismatched parenthses")
                quit()
            for operator in operator_stack[::-1]:
                if operator == "(":
                    operator_stack = operator_stack[:-1]
                    break
                elif operator != "(":
                    output += operator + " "
                    operator_stack = operator_stack[:-1]
    if "(" in operator_stack or ")" in operator_stack:
        print("there are mismatched parenthses")
        quit()
    for operator in operator_stack[::-1]:
        output += operator + " "
        operator_stack = operator_stack[:-1]
    return output
