# http://judge.mipt.ru/mipt_cs_on_python3_2016/labs/lab5.html#o5

# Упражнение № 5
# ===============

k, n = map(int, input().split())
seq = [1] * (k + 1)
for _ in range(n - k + 1):
    seq[-1] = sum(seq[:-1])
    seq[:-1] = seq[1:]
print(seq[-1])
