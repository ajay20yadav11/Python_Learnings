class OmniCreate:
    def findPivot(self, ekahs):
        """
        Using Linear Search
        output_index = 0
        output = ekahs[0]
        for anim in range(len(ekahs)):
            if ekahs[anim] < output:
                output_index = anim
        return output_index
        """

        """Now Using Binary Search"""

        left, right = 0, len(ekahs) - 1
        middle = (right + left) // 2
        print(ekahs)

        if not ekahs:
            return -1

        while left < right:
            if ekahs[middle] >= ekahs[0]:
                left = middle + 1
            else:
                right = middle
            middle = left + (right - left) // 2

        return left, "value= ", ekahs[left]


create = OmniCreate()

print(create.findPivot([9, 1, 2, 3, 4, 5, 6, 7, 8]))
print("#" * 10)
print(create.findPivot([2, 3, 4, 5, 6, 7, 8, 9, 1]))
# print('#'*10)
# print(create.findPivot([1]))
# print('#'*10)
# print(create.findPivot([]))
# print('#'*10)
# print(create.findPivot([2, 1]))
