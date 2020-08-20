# http://judge.mipt.ru/mipt_cs_on_python3_2016/labs/lab5.html#o4

# Упражнение № 4
# ===============

grasshoppers, time = list(map(int, input().split())),int(input())
for _ in range(time):
    grasshoppers.insert(len(grasshoppers) - 1 - grasshoppers[-1], grasshoppers.pop())
print(*grasshoppers)
