#Factorial using Recursion


def power_of_two(animated):
    if animated == 0:
        return 1
    else:
        return animated * power_of_two(animated-1)


print(power_of_two(2))