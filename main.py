from timeit import Timer

# Завдання 1. Реалізувати функцію жадібного алгоритму find_coins_greedy.

def find_coins_greedy(sum: int, coins: list[int]) -> dict[int, int]:
    """Greedy algorithm function for issuing coins."""
    result = {}
    for coin in sorted(coins, reverse=True):
        while sum >= coin:
            result[coin] = result.get(coin, 0) + 1
            sum -= coin
    return result

# Завдання 2. Реалізувати функцію динамічного програмування find_min_coins. 

def find_min_coins(sum: int, coins: list[int]) -> dict[int, int]:
    """Dynamic programming function for coin dispensing."""

    min_coins = [float('inf')] * (sum + 1)

    used_coins = [-1] * (sum + 1)
    min_coins[0] = 0

    for coin in coins:
        for i in range(coin, sum + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                used_coins[i] = coin

    if used_coins[sum] == -1:
        return {}

    result = {}
    while sum > 0:
        coin = used_coins[sum]
        result[coin] = result.get(coin, 0) + 1
        sum -= coin

    return result

if __name__ == "__main__":
    coins = [50, 20, 10, 5, 2, 1]
    amount = 113

    t_greedy = Timer(lambda: find_coins_greedy(amount, coins))
    t_min = Timer(lambda: find_min_coins(amount, coins))
    print(f"Test for the amount {amount} and coins {coins}")
    print(f"\nGreedy algorithm execution time: {t_greedy.timeit(number=1) * 1e5:.2f} μs")
    print(f"Dynamic programming execution time: {t_min.timeit(number=1) * 1e5:.2f} μs")

# Test for the amount 113 and coins [50, 20, 10, 5, 2, 1]
# Greedy algorithm execution time: 1.04 μs
# Dynamic programming execution time: 6.85 μs

    coins_big = [4, 7, 23, 50, 100, 500, 1000]
    amount_big = 10000
    t_greedy_big = Timer(lambda: find_coins_greedy(amount_big, coins_big))
    t_min_big = Timer(lambda: find_min_coins(amount_big, coins_big))
    print(f"\n\nTest for the BIG amount {amount_big} and coins {coins_big}")
    print(f"\nGreedy algorithm execution time: {t_greedy_big.timeit(number=1) * 1e5:.2f} μs")
    print(f"Dynamic programming execution time: {t_min_big.timeit(number=1) * 1e5:.2f} μs")

# Test for the BIG amount 10000 and coins [4, 7, 23, 50, 100, 500, 1000]
# Greedy algorithm execution time: 0.57 μs
# Dynamic programming execution time: 939.83 μs

    coins_min = [3, 4, 5, 8]
    amount_min = 6
    coins_used_min = find_coins_greedy(amount_min, coins_min)
    t_greedy_min = Timer(lambda: find_coins_greedy(amount_min, coins_min))
    t_min_min = Timer(lambda: find_min_coins(amount_min, coins_min))
    print(f"\n\nTest for the MIN amount {amount_min} and coins {coins_min}")
    print(f"\nGreedy algorithm execution time: {t_greedy_min.timeit(number=1) * 1e5:.2f} μs")
    print(f"Dynamic programming execution time: {t_min_min.timeit(number=1) * 1e5:.2f} μs")

# Test for the MIN amount 6 and coins [3, 4, 5, 8]
# Greedy algorithm execution time: 0.33 μs
# Dynamic programming execution time: 0.89 μs
