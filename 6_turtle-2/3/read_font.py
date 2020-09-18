def destring_tuple(T):
    """
    str -> tuple
    '(1,0,1.25)' -> (1,0,1.25)
    """
    return tuple(map(float, T.strip("()").split(",")))


def destring_list(L):
    """
    list of str -> list of tuples
    ['(1,0,1.25)', '(1,0,1)'] -> [(1,0,1.25), (1,0,1)]
    """
    return list(map(destring_tuple, L))


def read_font(font_file):
    constants = dict()
    font = dict()
    with open(font_file, "r") as f:
        f.readline()
        for line in f:
            if line.rstrip() == "ENDDEF":
                break
            constant, value = line.split(";")
            constants[constant] = value

        for line in f:
            for constant, value in constants.items():   # сделать ч/з регулярные выражения
                line = line.replace(constant, value)
            data = line.strip().split(";")
            tuples_str = data[1:]
            font[data[0]] = destring_list(tuples_str)

    return font
