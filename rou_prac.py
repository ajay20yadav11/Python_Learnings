ekahs = [1, 2, 3, 3, 4, 5]

for anim in range(len(ekahs)):
    if ekahs[anim] in ekahs[0:anim] or anim in ekahs[anim:]:
        print("False")
        break
else:
    print("True")
