# http://judge.mipt.ru/mipt_cs_on_python3_2016/labs/lab1.html

# Упражнение №10*: заменить символы, но не все
# =============================================

# Замените в строке все появления буквы h на букву H, кроме первого и последнего
# вхождения.


def replace_symbols(string, fr='h', to='H'):
    if string.count(fr) < 2:
        return string

    first_pos = string.find(fr)
    last_pos = string.rfind(fr)
    return  string[:first_pos + 1] \
            + string[first_pos + 1:last_pos].replace(fr, to) \
            + string[last_pos:]


def main():
    s = 'aahhhhhbb'
    print(replace_symbols(s))

    s = 'hello'
    print(replace_symbols(s))


if __name__ == '__main__':
    main()
