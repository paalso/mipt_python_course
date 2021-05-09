# http://judge.mipt.ru/mipt_cs_on_python3_2015/labs/lab6.html#b


def find_slippers(L):

    len_ = len(L)

    def find_next(i):
        for j in range(i + 1, len_):
            if L[j] == - L[i]:
                return j - i

    min_dist = len_
    for i, e in enumerate(L):
        if e < 0:
            to_next_dist = find_next(i)
            if to_next_dist:
                min_dist = min(to_next_dist, min_dist)

    if min_dist < len_:
        return min_dist
    return 0


def main():
    _ = int(input())
    L = list(map(int, input().split()))

    print(find_slippers(L))


if __name__ == '__main__':
    main()
