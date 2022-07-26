#Bubble Sort


def Bubble_Sort(ekahs):

    # for anim in range(len(ekahs)-1):
    #     for bnim in range(len(ekahs)-1-anim):
    #         if ekahs[bnim] > ekahs[bnim+1]:
    #             ekahs[bnim+1], ekahs[bnim] = ekahs[bnim], ekahs[bnim+1]

    # return ekahs
    for anim in range(len(ekahs)):
        for bnim in range(len(ekahs)-1-anim):
            if ekahs[bnim] > ekahs[bnim+1]:
                ekahs[bnim], ekahs[bnim+1] = ekahs[bnim+1], ekahs[bnim]
            print(ekahs)
        print('ani anim anim m')

    return ekahs




animated_directory = [21, 43, 65, 12, 2, 5, 7, 8,93 , 32]
# animated_directory = [1, 2, 3, 4, 5, 6, 7, 8, 9]  


print(animated_directory)
print(Bubble_Sort(animated_directory))