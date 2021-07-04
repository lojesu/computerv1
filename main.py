import sys

from parsing import parsing
from reduce_equation import reduce_equation
from determinate_polynomial_degree import determinate_polynomial_degree
from resolve_equation import (
    resolve_degree_0,
    resolve_degree_1,
    resolve_degree_2
)


"""
main function, leakser and algo start here with different functions call
"""
if len(sys.argv) < 2:
    print("tk1kon! 1")
    quit()
elif len(sys.argv) == 2:
    if sys.argv[1] == "-h":
        print("Ceci est un HELP")
        quit()
    equation = parsing(sys.argv[1])
elif len(sys.argv) == 3:
    if len(sys.argv[1]) > 0 and sys.argv[1][0] == "-":
        if "h" in sys.argv[1]:
            print("Ceci est un HELP")
            quit()
        elif "n" not in sys.argv[1] and "f" not in sys.argv[1]:
            print("tk1kon! 3")
            quit()
    else:
        print("tk1kon! 4")
        quit()
    equation = parsing(sys.argv[2])
else:
    print("tk1kon! 2")
    quit()
    
reduced_form = reduce_equation(equation)
polynomial_degree = determinate_polynomial_degree(reduced_form)

reduced_form_print = ""
for token in reduced_form:
    if type(token) == tuple:
        if int(token[0]) == 1:
            reduced_form_print += "X^" + str(token[1]) + " "
        else:
            reduced_form_print += str(token[0]) + " * X^" + str(token[1]) + " "
    else:
        reduced_form_print += token + " "
if "n" in sys.argv[1]:
    reduced_form_print = reduced_form_print.replace("* X^0", "")
    reduced_form_print = reduced_form_print.replace("X^1", "X")
reduced_form_print += "= 0"

print("Reduced form :", reduced_form_print)
print("Polynomial degre :", polynomial_degree)

if polynomial_degree == 2:
    resolve_degree_2(reduced_form)
elif polynomial_degree == 1:
    resolve_degree_1(reduced_form)
elif polynomial_degree == 0:
    resolve_degree_0(reduced_form, equation)
