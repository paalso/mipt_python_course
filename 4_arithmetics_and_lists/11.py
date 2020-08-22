# http://judge.mipt.ru/mipt_cs_on_python3_2016/labs/lab5.html#o12

# Упражнение №12 (небоскребы)
# ============================

# находит следующую позицию массива, значение к-й == 0
def findNextZero(L, startIndex, value=0):
    try:
        zeroPos = L[startIndex:].index(value)
        return startIndex + zeroPos
    except:
        return len(L)


def findNextNonZero(L, startIndex, value=0):
    for i in range(startIndex, len(L)):
        if L[i] != value:
            return i
    return -1


def lookOverRects(L, startPos, endPos):
    """
    Перебирает все прямоугольники, начиная с точки startPos до точки endPos
    (включительно) направо и вверх
    Возвращает tuple (максимальная площадь, высота)
              *
          *   *
        * **  **
        ****  ***
        *********
    """
    segmentData = []
    for startPos in range(startPos, endPos + 1):
        for i in range(1, endPos - startPos + 2):
            height = min(L[startPos:startPos + i])
            segmentData.append((height * i, height))
    return max(segmentData, key=lambda t: t[0])

testData = (
        ([5, 8, 7, 6, 5, 4], (25, 5)),
        ([1, 2, 8], (8, 8)),
        ([1], (1, 1)),
        ([1, 0, 0, 1, 0], (1, 1)),
        ([1, 0, 0, 1, 2], (2, 1)),
        ([1, 2, 3, 4], (6, 2)),
        ([1, 2, 3, 4, 5], (9, 3)),
        ([5, 4, 3, 2, 1], (9, 3)),
        ([0, 3, 2, 4, 4, 1, 0, 8], (8, 2)),
        ([0, 3, 2, 4, 4, 1, 0, 9], (9, 9)),
        ([1, 9, 4, 1, 5, 5, 1, 1], (10, 5)),
        ([1, 9, 6, 1, 5, 5, 1, 1], (12, 6)),
        ([1, 9, 4, 1, 5, 5, 1, 1, 1, 1, 1], (11, 1)),
    )

try:
    for (heights, result) in testData:
        # sprint(lookOverRects(heights, 0, len(heights) - 1))
        assert lookOverRects(heights, 0, len(heights) - 1) == result
    print("Работает ОК")
except:
    print("Что то не так")
