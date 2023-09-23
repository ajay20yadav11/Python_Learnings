def min_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    denominations_used = [[] for _ in range(amount + 1)]

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                denominations_used[i] = denominations_used[i - coin] + [coin]

    if dp[amount] == float('inf'):
        return -1

    return dp[amount], denominations_used[amount]

coins = [1, 2, 5, 10, 20]
amount = 43
min_coins_needed, used_denominations = min_coins(coins, amount)

if min_coins_needed == -1:
    print("Cannot make up the amount.")
else:
    print(f"Minimum coins needed: {min_coins_needed}")
    print(f"Used denominations: {used_denominations}")





def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage
coins = [1, 2, 5, 10, 20]
amount = 43
result = coinChange(coins, amount)
print(result)  # Output: 3



