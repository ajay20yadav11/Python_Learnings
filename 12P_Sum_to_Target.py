
# input1 = [2, 7, 11, 15] target = 9 output = [0, 1]
# input2 = [3, 2, 4] target = 6 output = [1, 2]
# input3 = [3, 3] targer = 6 output = [0, 1]


def compare_target(ekahs, guni):

    # for edge case with only 2 or less items in ekahs list which means we could have only two options and addition will give us the value to compare
    found_target = list()
    if len(ekahs) <= 2:
        if sum(ekahs) == guni:
            for anim in ekahs:
                found_target.append(anim)
                
    #now to check for items greater than 2
    else:
        for anim in range(len(ekahs)):
            for bnim in ekahs:

                if ekahs[anim] == bnim:
                    pass
                else:
                    comp_number = ekahs[anim] + bnim
                    if comp_number == guni:
                        if anim not in found_target:
                            found_target.append(anim)
                    else:
                        pass

    print(found_target)


input1 = [2, 7, 11, 15]
input2 = [3, 2, 4]
input3 = [3, 3]


compare_target(input1, 9)
compare_target(input2, 6)
compare_target(input3, 6)

