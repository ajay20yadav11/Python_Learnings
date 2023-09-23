def max_elements_sum_target(target, elements):
    elements.sort(reverse=True)

    def backtrack(curr_sum, start_idx):
        if curr_sum == target:
            return 0

        max_elements = 0
        for i in range(start_idx, len(elements)):
            if curr_sum + elements[i] <= target:
                num_elements = backtrack(curr_sum + elements[i], i + 1)
                max_elements = max(max_elements, num_elements + 1)

        return max_elements

    return backtrack(0, 0)

# Test the function
elements = [2, 3, 5, 5]
target = 5
result = max_elements_sum_target(target, elements)
print(result)
