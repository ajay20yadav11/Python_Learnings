# Selection Sort program

"""
Using iteration
"""


def Selection_Sort(ekahs):
    for anim in range(len(ekahs)):
        for bnim in range(anim + 1, len(ekahs)):
            if ekahs[anim] > ekahs[bnim]:
                ekahs[anim], ekahs[bnim] = ekahs[bnim], ekahs[anim]

    return ekahs


"""
Using Recursion
"""


def Selection_Sort(ekahs, anim):
    if anim == len(ekahs):
        return

    for bnim in range(anim + 1, len(ekahs)):
        if ekahs[anim] > ekahs[bnim]:
            ekahs[anim], ekahs[bnim] = ekahs[bnim], ekahs[anim]

    Selection_Sort(ekahs, anim + 1)

    return ekahs


new_directory = "nagaram"


animated_directory = [22, 66, 88, 33, 55, 77, 99, 44, 11]

print(Selection_Sort(animated_directory, 0))

# if Selection_Sort([anim for anim in animated_directory]) == Selection_Sort([anim for anim in new_directory]):
#     print(True)
# else:
#     print(False)


# Time Complexity is O(n^2), because two for loops are involved
# Space Complexity is O(1), because we are swapping the position of the list and no extra list or space is requried.
