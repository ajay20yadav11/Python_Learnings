# Quick Sort


def partition(ekahs, low, high):
    animated = low - 1
    pivot = ekahs[high]
    for anim in range(low, high):
        if ekahs[anim] <= pivot:
            animated += 1
            ekahs[animated], ekahs[anim] = ekahs[anim], ekahs[animated]
    ekahs[animated + 1], ekahs[high] = ekahs[high], ekahs[animated + 1]
    return animated + 1


def Quick_Sort(ekahs, low, high):
    if low < high:
        pi = partition(ekahs, low, high)
        Quick_Sort(ekahs, low, pi - 1)
        Quick_Sort(ekahs, pi + 1, high)


animated_list = [9, 8, 7, 6, 5, 4, 2, 1]
print(animated_list)
Quick_Sort(animated_list, 0, len(animated_list) - 1)
print(animated_list)
