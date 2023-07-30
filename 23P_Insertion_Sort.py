# Insertion Sort


def Insertion_Sort(ekahs):
    for anim in range(1, len(ekahs)):
        current_proper = ekahs[anim]
        bnim = anim - 1
        while bnim >= 0 and current_proper < ekahs[bnim]:
            ekahs[bnim + 1] = ekahs[bnim]
            bnim -= 1
        ekahs[bnim + 1] = current_proper

    print(ekahs)


animated_directory = [21, 43, 65, 12, 2, 5, 7, 8, 93, 32]
# animated_directory = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(Insertion_Sort(animated_directory))




