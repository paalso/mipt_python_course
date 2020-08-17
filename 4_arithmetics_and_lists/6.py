# http://judge.mipt.ru/mipt_cs_on_python3_2016/labs/lab5.html#o6

# Упражнение № 6
# ===============


def get_median(L):
    for item in L:
        counter = 0
        for el in L:
            if el == item:
                continue
            counter += 1 if el > item else -1
        if counter == 0:
            return item


data = [
    "6 1 9 2 3 4 8",
    "1",
    "1 2 3",
    "10 0 11 1 5"]

for el in data:
    L = list(map(int, el.split()))
    print(get_median(L))
