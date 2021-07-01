import sys

from parsing import parsing
from reduce_equation import reduce_equation
from determinate_polynomial_degree import determinate_polynomial_degree
from resolve_degree_2 import resolve_degree_2


"""
main function, algo start here with different functions call
"""
if len(sys.argv) < 2:
    print("tk1kon! 1")
    quit()
elif len(sys.argv) == 2:
    if sys.argv[1] == "-h":
        print("Ceci est un HELP")
        quit()
    equation = parsing(sys.argv[1])
else:
    print("tk1kon! 2")
    
reduced_form = reduce_equation(equation)
polynomial_degree = determinate_polynomial_degree(reduced_form)

# je dois faire print reduce form correctement
print(reduced_form)
print("Polynomial degre :", polynomial_degree)

if polynomial_degree == 2:
    resolve_degree_2(reduced_form)
