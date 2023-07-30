# House Robber

def house_robber(houses):
    if not houses:
        return 0
    
    n = len(houses)
    dp = [0] * n
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i - 2] + houses[i])
    return dp[n - 1]


if __name__ == "__main__":
  houses = [1, 2, 3, 1]
  print(house_robber(houses))


def House_Robber(nums) -> str:
    ODD_adjacent = 0
    EVEN_adjacent = 0

    if len(nums) == 1:
        return nums[0]
    else:
        for anim in range(-1, len(nums) - 1, 2):
            ODD_adjacent += nums[anim + 1]

        for anim in range(0, len(nums) - 1, 2):
            EVEN_adjacent += nums[anim + 1]

        if ODD_adjacent > EVEN_adjacent:
            return f"Max Amount can be drawn is ODD combination: {ODD_adjacent}"
        elif ODD_adjacent == EVEN_adjacent:
            return f"Max Amount can be drawn is any combination: {EVEN_adjacent}"
        else:
            return f"Max Amount can be drawn is EVEN combination: {EVEN_adjacent}"


animated = [1, 2, 3, 4]


print(House_Robber(animated))
