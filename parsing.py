from calcul import is_operator


"""
this function delete multispace in a string
"""
def despace(str):
    while "  " in str:
        str = str.replace("  "," ")
    return str


"""
principal parsing function for computerv1
"""
def parsing(str):
    str = despace(str)
    if str.count("=") != 1:
            print("CONNARD! 1")
            quit()
    i = 0
    for char in str:
        if is_operator(char) == False and char.isdigit() == False \
            and char != "X" and char != " " and char != "=" and char != ".":
            print("CONNARD! 2")
            quit()
        if char == "^" and i < len(str) - 2 and (str[i + 1] == "X" or str[i + 2] == "X"):
            print("CONNARD! 3")
            quit()
        if char == "." and (i <= 0 or i >= len(str) - 1 \
            or str[i - 1].isdigit() == False or str[i + 1] == False):
            print("CONNARD! 4")
            quit()
        i += 1

    str = formatting(str)
    str_split = str.split()
    i = 1
    for token in str_split:
        if i % 2 == 0:
            if is_operator(token) == False and token != "=" \
                or token == "^":
                print("CONNARD! 5")
                quit()
        if i % 2 == 1:
            if is_operator(token) == True or token == "=":
                print("CONNARD! 6")
                quit()
        if i == len(str_split):
            if token == "=":
                print("CONNARD! 7")
                quit()
        i += 1
    str = Xformatting(str)
    return str

"""
this function convert X to X^1 for the rest of the code
"""
def Xformatting(str):
    i = 0
    str_split = str.split()
    for token in str_split:
        if token == "X":
            str_split[i] = "X^1"
        i += 1
    return " ".join(str_split)


"""
this function return the calcul correctly formatted for the rest
"""
def formatting(str):
    new_str = ""
    i = 0
    for char in str:
        if char == "-":
            if str[i + 1].isdigit() or str[i + 1] == "X":
                new_str += char
            else:
                new_str += char + " "
        elif char.isdigit() or char == ".":
            if  i < len(str) - 1 and (str[i + 1].isdigit() or str[i + 1] == "."):
                new_str += char
            else:
                new_str += char + " "
        elif char != " ":
            if char == "X" or (char == "^" and i > 1 and str[i - 1] == "X" or str[i - 2] == "X"):
                if i < len(str) - 2 and (str[i + 1] == "=" \
                    or (str[i + 2] == "=" and str[i + 1] == " ")):
                    new_str += char + " "
                else:
                    new_str += char
            else:
                new_str += char + " "
        i += 1
    return new_str
