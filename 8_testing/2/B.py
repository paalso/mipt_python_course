# http://judge.mipt.ru/mipt_cs_on_python3_2015/labs/lab6.html#b


def find_coins_demand(array):
    current_change_coins = 0
    coins_lack = 0
    max_coins_lack = 0

    for e in array:
        coins_get = e // 5
        coins_to_return = coins_get - 1
        coins_lack = max(coins_to_return - current_change_coins, 0)
        max_coins_lack = max(max_coins_lack, coins_lack)
        current_change_coins = current_change_coins + \
                1 if coins_get == 1 else 0 - coins_lack

    return max_coins_lack


def main():
    _ = int(input())
    array = list(map(int, input().split()))

    print(find_coins_demand(array))


if __name__ == '__main__':
    main()
