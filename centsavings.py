import math

def round_to_nearest_10(total):
    remainder = total % 10
    if remainder >= 5:
        return total + (10 - remainder)
    return total - remainder

def calculate_min_cost(num_items, num_dividers, prices):
    dp = [[float('inf')] * (num_dividers + 1) for _ in range(num_items + 1)]

    for divider in range(num_dividers + 1):
        dp[0][divider] = 0

    for item in range(1, num_items + 1):
        dp[item][0] = dp[item - 1][0] + prices[item - 1]

    for item in range(1, num_items + 1):
        for divider in range(num_dividers, 0, -1):
            dp[item][divider] = min(
                dp[item - 1][divider] + prices[item - 1],
                round_to_nearest_10(dp[item - 1][divider - 1] + prices[item - 1])  # Add a new divider
            )

    min_cost = float('inf')
    for divider in range(num_dividers + 1):
        min_cost = min(min_cost, round_to_nearest_10(dp[num_items][divider]))

    return min_cost

def main():
    num_items, num_dividers = map(int, input().split())
    prices = list(map(int, input().split()))

    result = calculate_min_cost(num_items, num_dividers, prices)
    print(result)

if __name__ == "__main__":
    main()
