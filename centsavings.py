# solution for Cent Savings
import sys
inf = float('inf')
def rounded_cost(n):
    left = n % 10
    if left >= 5:
        return n + (10 - left)
    return n - left

def main():
    n, m = map(int, input().split())
    v = list(map(int, input().split()))
    memo = [[inf] * (m + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        memo[0][i] = 0