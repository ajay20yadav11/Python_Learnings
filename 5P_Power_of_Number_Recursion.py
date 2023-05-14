def find_power(animated, banimated):
    if banimated == 0:
        return 1
    if banimated == 1:
        return animated

    return animated * find_power(animated, banimated - 1)


print(
    find_power(
        int(input("Enter number to number: ")), int(input("Enter the value of index: "))
    )
)
