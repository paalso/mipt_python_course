http://judge.mipt.ru/mipt_cs_on_python3_2015/labs/lab6.html#d


def read_matrix(n):
    return [list(map(int, input().split())) for _ in range(n)]


def find_minimums_in_columns(matrix):
    minimums_in_columns = []
    for col in range(len(matrix[0])):
        min_ = matrix[0][col]
        for row in range(len(matrix)):
            min_ = min(min_, matrix[row][col])
        minimums_in_columns.append(min_)
    return minimums_in_columns


k, _ = map(int, input().split())
matrix = read_matrix(k)
print(*find_minimums_in_columns(matrix))
