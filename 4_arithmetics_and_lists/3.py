# http://judge.mipt.ru/mipt_cs_on_python3_2016/labs/lab5.html#o3

# Упражнение №3
# =================================

# Вывести список в следующем порядке: первое число, последнее, второе,
# предпоследнее и так далее все числа.

# 1 2 3 4 5	->  1 5 2 4 3
# 1 2 3 4 ->  1 4 2 3

s = "1 2 3 4 5 6 7"
s = "1 2 3 4 5 6"
s = "1 2 3 4"
s = "1 2 3 4 5"
L = s.split()

L[::2], L[1::2] = L[:(len(L) + 1) // 2:], L[-1:(len(L) - 1) // 2:-1]
print(*L)

# Авторское решение
# A[::2], A[1::2] = A[:(len(A) + 1)//2], A[(len(A) + 1)//2:][::-1]
# Таки лучше, т.к. логичнее