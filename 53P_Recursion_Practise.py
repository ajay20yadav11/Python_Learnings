
def recursionPractice(ekahs):

    if ekahs == 0:
        return 1
    if ekahs == 1:
        return 1
    
    vall =  recursionPractice(ekahs-1)
    return vall + recursionPractice(ekahs-2)


print(recursionPractice(20))