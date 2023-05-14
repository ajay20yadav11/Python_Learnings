# from abc import abstractproperty


# Three steps to create two dimesional array.
# 1. Assign it to a variable
# 2. Define the type of elements it will store
# 3. Define its size

from array import *
import numpy as np

# 1. Created two dimesional array
two_D_Array = np.array(
    [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34], [41, 42, 43, 44]]
)

# 2. Insertion of value in 2D array. Time complexity is O(mn), m is column and n is row. Using append() we can add column or row at last

new_2D_Array = np.insert(
    two_D_Array, 0, [[1, 2, 3, 4]], axis=0
)  # 0 for row and 1 for column

new_2D_Array = np.append(
    two_D_Array, [[51, 53, 53, 54]], axis=0
)  # Using append we can add column or row at last

# 3. To travere 2D Array

for anim in new_2D_Array:
    for bnim in anim:
        new_bnim = []
        new_bnim = bnim

# 4. Searching 2 D Array

for anim in range(len(two_D_Array)):
    for bnim in range(len(two_D_Array[0])):
        if two_D_Array[anim][bnim] == 43:
            new_index = int()

# 5. To Delete 2 D array


new_deleted_array = np.delete(two_D_Array, 0, axis=1)
