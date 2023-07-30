# Merge Sort

# We will require two function
# 1. To divide the array into last extent------------first function
# 2. Sorted the array using the second function
# 3. To merge the sorted array--------------------second function

def merge_sort(ekahs):
    if len(ekahs) <= 1:
        return ekahs

    middle = len(ekahs) // 2
    left_half = ekahs[:middle]
    right_half = ekahs[middle:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    return merged

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)