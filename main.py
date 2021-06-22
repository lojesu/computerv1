import sys

from parsing import parsing
from reduce_equation import reduce_equation


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

print(equation)
print(reduced_form)
