# House Robber


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


animated = []


print(House_Robber(animated))
