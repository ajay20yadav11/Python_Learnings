
def find_sum_of_digit(animated):

    if int(animated) == 0:
        return 0

    return find_sum_of_digit(int(animated) / 10) + int(animated) % 10


print(find_sum_of_digit(int(input('Enter the number to sum: '))))