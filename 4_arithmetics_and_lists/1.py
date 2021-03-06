# http://judge.mipt.ru/mipt_cs_on_python3_2016/labs/lab5.html

# Упражнение №1. Однострочники
# =============================

s = "1 2 3 4 5"
L = s.split()

# Выведите элементы списка с чётными индексами.
print(*L[::2])      # 1 3 5

# Найдите наибольший элемент в списке. Выведите значение элемента и его индекс.
s = "1 2 3 4 5 1 2 0"
L = s.split()
print(max(L), L.index(max(L)))      # 5 4

# Выведите список в обратном порядке
s = "1 2 3 4 5"
L = s.split()
print(*L[::-1])      # 5 4 3 2 1
