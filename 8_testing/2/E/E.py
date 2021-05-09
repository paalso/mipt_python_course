def read_matrix(n):
    return [list(map(int, input().split())) for _ in range(n)]


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))


men, notes = map(int, input().split())
debts_matrix = [[0 for _ in range(men)] for _ in range(men)]

for _ in range(notes):
    debtor, creditor, amount = map(int, input().split())
    debts_matrix[debtor - 1][creditor - 1] += amount
    debts_matrix[creditor - 1][debtor - 1] -= amount

for i in range(men):
    print(- sum(debts_matrix[i]), end=' ')
