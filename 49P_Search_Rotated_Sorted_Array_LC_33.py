class OmniCreate:
    def searchRotSorted(self, ekahs, target):
        def findPivot(self, ekahs):
            left, right = 0, len(ekahs) - 1
            middle = (right - left) // 2

            if not ekahs:
                return -1

            while left < right:
                if ekahs[middle] >= ekahs[0]:
                    left = middle + 1
                else:
                    right = middle
                middle = left + (right - left) // 2

            return left

        def BinarySearch(self, ekahs, left, right, target):
            middle = (right - left) // 2

            while left < right:
                if ekahs[middle] == target:
                    return middle
                elif ekahs[middle] < target:
                    left = middle + 1
                else:
                    right = middle

                middle = left + (right - left) // 2

            return left

        print(ekahs)
        pivot = findPivot(self, ekahs)

        left, right = 0, len(ekahs) - 1
        if ekahs[pivot] < target <= ekahs[right]:
            return BinarySearch(self, ekahs, pivot, right, target)

        else:
            return BinarySearch(self, ekahs, left, pivot - 1, target)


create = OmniCreate()

print(create.searchRotSorted([9, 1, 2, 3, 4, 5, 7, 8], int(input("enter: "))))
