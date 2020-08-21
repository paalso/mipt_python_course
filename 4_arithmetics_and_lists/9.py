# http://judge.mipt.ru/mipt_cs_on_python3_2016/labs/lab5.html#o9

# Упражнение № 9
# ===============

hours = int(input())
data = list(map(int, input().split()))
k = int(input())

maximum = max([sum(data[i:i + k]) for i in range(hours - k + 1)])
print(maximum)
