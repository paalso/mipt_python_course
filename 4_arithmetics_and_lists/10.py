# http://judge.mipt.ru/mipt_cs_on_python3_2016/labs/lab5.html#o10

# Упражнение № 10
# ===============


def print_pascal_triangle(n):
    prev_list = [1]
    print(*prev_list)
    for i in range(1, n + 1):
        L = [1]
        for j in range(1, i):
            L.append(prev_list[j - 1] + prev_list[j])
        L.append(1)
        print(*L)
        prev_list = L


N = 6
print_pascal_triangle(N)
