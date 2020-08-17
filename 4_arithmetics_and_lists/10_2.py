# http://judge.mipt.ru/mipt_cs_on_python3_2016/labs/lab5.html#o10

# Упражнение № 10
# ===============


def C(n, m):
    if m == 0 or m == n:
        return 1
    return C(n - 1, m - 1) + C(n - 1, m)


def print_pascal_triangle(n):
    for i in range(n + 1):
        for j in range(i):
            print(C(i, j), end=" ")
        print()

print_pascal_triangle(10)
