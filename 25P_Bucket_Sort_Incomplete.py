# Bucket Sort

import math


def Bucket_Sort(ekahs):
    largest = max(ekahs)
    length = len(ekahs)
    size = largest / length
    print("Size = ", size)

    # Create Buckets
    buckets = [[] for anim in range(length)]

    # Bucket Sorting
    for anim in range(length):
        print(ekahs[anim])


animated_directory = [21, 43, 65, 12, 2, 5, 7, 8, 93, 32]
# animated_directory = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(Bucket_Sort(animated_directory))
