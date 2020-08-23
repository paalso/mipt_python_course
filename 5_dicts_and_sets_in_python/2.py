# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab23.html#o2
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab18.html#o3

# Упражнение № 2
# ===============

# Даны четыре множества:
A = set('0123456789')
B = set('02468')
C = set('12345')
D = set('56789')

# Найти элементы, принадлежащие множеству E:

E = ((A - B) & (C - D)) | ((D - A) & (B - C))
print(*E)
