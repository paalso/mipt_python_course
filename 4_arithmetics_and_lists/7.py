# http://judge.mipt.ru/mipt_cs_on_python3_2016/labs/lab5.html#o7

# Упражнение № 7
# ===============

def get_final_grade(data):
    counter = 0     # счетчик исправленных двоек
    for i in range(len(data) - 1):
        if data[i] == 2 and data[i + 1] > 2:
            counter += 1
    return int((sum(data) - counter * 2) / (len(data) - counter))


##data = tuple(map(int, input().split()))
##print(get_final_grade(data))

try:
    assert get_final_grade([2, 5, 2, 5, 2, 5, 2, 5, 2, 5]) == 5
    assert get_final_grade([2, 2, 2, 2, 2, 2, 2, 2, 2, 5]) == 2
    assert get_final_grade([5, 5, 5, 5, 5, 5, 5, 5, 5, 2]) == 4
    print("All is OK")
except AssertionError:
    print("Look for a mistake")