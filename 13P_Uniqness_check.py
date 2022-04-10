import numpy as np

# [[1 2 3]
# [4 5 6]
# [7 8 9]]



orig_array = np.array([[1, 2, 3], [4, 5, 6] ,[7 ,8, 9]])
print(orig_array)

change_row_to_col = np.zeros(shape=(3,3))

rotate_array = np.zeros(shape=(3 ,3))

#convert row into column
for anim in range(len(orig_array)):
    for bnim in range(len(orig_array[0])):
        change_row_to_col[anim][bnim] = orig_array[bnim][anim]

count_of_array = len(orig_array) - 1

for anim in range(len(orig_array)):

    for bnim in range(len(orig_array[0])):
        rotate_array[anim][bnim] = orig_array[bnim][count_of_array]
    
    count_of_array = count_of_array - 1


print(rotate_array)