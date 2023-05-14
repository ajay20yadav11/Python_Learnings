class OmniCreate:
    def peakIndexInMountainArray(self, arr):
        """output = arr[0]
        output_index = 0
        for anim in range(len(arr)):
            if arr[anim] > output:
                output = arr[anim]
                output_index = anim
        return output_index"""

        left, right = 0, len(arr) - 1
        middle = left + (right - left) // 2

        while left < right:
            if arr[middle] < arr[middle + 1]:
                left = middle + 1
            else:
                right = middle

            middle = left + (right - left) // 2

        return left


create = OmniCreate()

print(create.peakIndexInMountainArray([24, 69, 100, 71, 72, 74, 100, 88]))
