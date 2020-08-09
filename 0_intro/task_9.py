# http://judge.mipt.ru/mipt_cs_on_python3_2016/labs/lab1.html

# Упражнение №9*: вставить *
# ===========================

# Получите новую строку, вставив между двумя символами исходной строки символ *.
# Выведите полученную строку.

def ins_even_sym(string, sym='*'):
    return sym.join(list(string))


def main():
    s = 'python'
    print(ins_even_sym(s))

    s = 'Hello'
    print(ins_even_sym(s))


if __name__ == '__main__':
    main()
