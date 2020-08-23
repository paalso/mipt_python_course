# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab23.html#o1
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab18.html#o2

# Упражнение № 1
# ===============

# Вывести на экран все элементы множества A, которых нет в множестве B.

A = set('bqlpzlkwehrlulsdhfliuywemrlkjhsdlfjhlzxcovt')
B = set('zmxcvnboaiyerjhbziuxdytvasenbriutsdvinjhgik')

print(*[a for a in A if a not in B])
print(* A.difference(B))
