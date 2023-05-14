# Merge Sort

# We will require two function
# 1. To divide the array into last extent------------first function
# 2. Sorted the array using the second function
# 3. To merge the sorted array--------------------second function


def Merge(
    ekahs, left_index, middle_index, right_index
):  # Function to merge the divided array
    n1 = middle_index - left_index + 1
    n2 = right_index - middle_index

    left_array = [0] * (n1)
    right_array = [0] * (n2)

    for anim in range(0, n1):
        left_array[anim] = ekahs[left_index + anim]

    for bnim in range(0, n2):
        right_array[bnim] = ekahs[middle_index + 1 + bnim]

    anim = 0
    bnim = 0
    madhya = left_index

    while anim < n1 and bnim < n2:
        if left_array[anim] <= right_array[bnim]:
            ekahs[madhya] = left_array[anim]
            anim += 1
        else:
            ekahs[madhya] = right_array[bnim]
            bnim += 1

        madhya += 1

    while anim < n1:
        ekahs[madhya] = left_array[anim]
        madhya += 1
        anim += 1

    while bnim < n2:
        ekahs[madhya] = right_array[bnim]
        madhya += 1
        bnim += 1

    return ekahs


# Function to apply sorting in a given divided array
def Merge_Sort(ekahs, left_index, right_index):
    if left_index < right_index:
        middle_index = (left_index + (right_index - 1)) // 2

        Merge_Sort(ekahs, left_index, middle_index)
        Merge_Sort(ekahs, middle_index + 1, right_index)
        Merge(ekahs, left_index, middle_index, right_index)

    return ekahs


animated_directory = [21, 43, 65, 12, 2, 5, 7, 8, 93, 32]
# animated_directory = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(animated_directory)

print(Merge_Sort(animated_directory, 0, len(animated_directory) - 1))
