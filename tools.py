"""
function for determinate if the tokken is an operator
"""
def is_operator(token):
    if token == "+" or token == "-" or token =="*" or token == "/" or token == "^":
        return True
    return False


"""
return second element of elem
"""
def take_second(elem):
    return elem[1]


"""
return first element of elem
"""
def take_first(elem):
    return elem[0]


