def is_operator(token):
    if token == "+" or token == "-" or token =="*" or token == "/" or token == "^":
        return True
    return False


def parsing(str):
    if str.count("=") != 1:
            print("CONNARD!")
            quit()
    for char in str:
        if is_operator(char) == False and char.isdigit() == False \
            and char != "X" and char != " " and char != "=":
            print("CONNARD!")
            quit()

    new_str = ""
    i = 0
    for char in str:
        if char.isdigit() and  i != len(str) - 1 and str[i + 1].isdigit():
            new_str += char
        elif char != " ":
            if char == "X" or (char == "^" and str[i - 1] == "X"):
                new_str += char
            else:
                new_str += char + " "
        i += 1
    print(new_str)



parsing("5*X^0 +4 * X^1 -9 *X^2 =1 * X^0")
