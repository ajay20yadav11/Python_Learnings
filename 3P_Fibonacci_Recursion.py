def find_fibonacci(animated):

    if animated == 0 or animated == 1:
        return 1
    
    return find_fibonacci(animated-1) + find_fibonacci(animated-2)


print(find_fibonacci(int(input('Enter number: '))))
