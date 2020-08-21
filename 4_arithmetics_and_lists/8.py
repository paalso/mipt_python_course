# http://judge.mipt.ru/mipt_cs_on_python3_2016/labs/lab5.html#o8

# Упражнение № 8
# ===============

passengers_moving_data = []

n = int(input())
for _ in range(n):
    in_time, out_time = map(int, input().split())
    passengers_moving_data.append((in_time, out_time))

final_time = max(map(lambda t: t[1], passengers_moving_data))

passengers_staying_data = [0] * (final_time + 1)

for in_time, out_time in passengers_moving_data:
    for minute in range(in_time, out_time + 1):
        passengers_staying_data[minute] += 1

# print(passengers_staying_data)

minute = int(input())
print(passengers_staying_data[minute])
