"""
http://judge.mipt.ru/mipt_cs_on_python3_2015/labs/lab6.html#a

В массиве ровно два элемента равны. Найдите эти элементы.
Программа получает на вход число N, в следующей строке заданы N элементов
списка через пробел.
Выведите значение совпадающих элементов.
"""


def find_two_equal(array):
    array_copy = array[:]
    array_copy.sort()
    for i in range(1, len(array_copy)):
        if array_copy[i] == array_copy[i - 1]:
            return array_copy[i]


def main():
    _ = int(input())
    array = list(map(int, input().split()))
    print(find_two_equal(array))


if __name__ == '__main__':
    main()
