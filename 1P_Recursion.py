# Program to find A raise to B using recursion

def finding_power_solution(a, b):
    #Base Condition to break Recursion Loop
    if b == 0: 
        return 1

    else:
        return a * finding_power_solution(a, b-1)
        

print('Value of Power: ' + str(finding_power_solution(int(input('Enter a: ')), int(input('Enter b: ')))))