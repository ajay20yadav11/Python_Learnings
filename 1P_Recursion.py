# Program to find A raise to B using recursion

def finding_power_solution(a, b):
    if b == 0:
        return 1

    else:
        return a * finding_power_solution(a, b-1)
        

print(finding_power_solution(int(input('Enter a: ')), int(input('Enter b '))))