import sys

from parsing import parsing
from reduce_equation import reduce_equation
from determinate_polynomial_degree import determinate_polynomial_degree
from resolve_equation import (
    resolve_degree_0,
    resolve_degree_1,
    resolve_degree_2,
    number_to_fraction
)

"""
function for print the helper
"""
def print_helper():
    print("USAGE: python3 main.py [OPTIONS] [OPERATION]\n")
    print("OPTIONS:")
    print("\t-n\tfor simplify reduced form display")
    print("\t-f\twrite the result as fraction if possible")
    print("\t-h\tdisplay help information\n")

"""
main function, leakser and algo start here with different functions call
"""
if len(sys.argv) < 2:
    print("you don't have enough argument")
    quit()
elif len(sys.argv) == 2:
    if sys.argv[1] == "-h":
        print_helper()
        quit()
    equation = parsing(sys.argv[1])
elif len(sys.argv) == 3:
    if len(sys.argv[1]) > 0 and sys.argv[1][0] == "-":
        if "h" in sys.argv[1]:
            print_helper()
            quit()
        elif "n" not in sys.argv[1] and "f" not in sys.argv[1]:
            print("you put a wrong option")
            quit()
    else:
        print_helper()
        quit()
    equation = parsing(sys.argv[2])
else:
    print("you have too much argument")
    quit()
    
reduced_form = reduce_equation(equation)
polynomial_degree = determinate_polynomial_degree(reduced_form)

reduced_form_print = ""
for token in reduced_form:
    if type(token) == tuple:
        if token[1] % 1 != 0:
            print("we don't resolve equation with non integer power'")
            quit()
        if int(token[0]) == 1:
            reduced_form_print += "X^" + str(int(token[1])) + " "
        else:
            if "n" in sys.argv[1]:
                reduced_form_print += str(number_to_fraction(token[0])) + " * X^" + str(int(token[1])) + " "
            else:
                reduced_form_print += str(token[0]) + " * X^" + str(int(token[1])) + " "
    else:
        reduced_form_print += token + " "
if "n" in sys.argv[1]:
    reduced_form_print = reduced_form_print.replace(" * X^0", "")
    reduced_form_print = reduced_form_print.replace("X^1", "X")
reduced_form_print += "= 0"

print("Reduced form :", reduced_form_print)
print("Polynomial degre :", polynomial_degree)

if polynomial_degree == 2:
    resolve_degree_2(reduced_form, sys.argv[1][1:])
elif polynomial_degree == 1:
    resolve_degree_1(reduced_form, sys.argv[1][1:])
elif polynomial_degree == 0:
    resolve_degree_0(reduced_form, equation)
