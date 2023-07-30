class OmniCreate:
    """
    Given an array of non-negative integers height, where height[i] represents the height of the line at position i,
    find two lines, which together with the x-axis, forms a container such that the container contains the most water.
    Example:
    Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    Output: 49
    """

    def maxContainer(self, ekahs):
        left, right = 0, len(ekahs) - 1
        max_area = 0

        while left < right:
            current_height = min(ekahs[left], ekahs[right])
            current_width = right - left
            current_area = current_height * current_width
            max_area = max(max_area, current_area)

            if ekahs[left] < ekahs[right]:
                left += 1
            else:
                right -= 1

        return max_area


if __name__ == "__main__":
    create = OmniCreate()
    print(create.maxContainer([1, 8, 6, 2, 5, 4, 8, 3, 7]))
