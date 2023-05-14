class OmniCreate:
    def Search_Insert_Index(self, ekahs, target):
        left, right = 0, len(ekahs)
        middle = (right + left) // 2
        if len(ekahs) == 0:
            return 0
        while left < right:
            if ekahs[middle] == target:
                return middle
            elif ekahs[middle] < target:
                left = middle + 1
            else:
                right = middle
            middle = (right + left) // 2
        return left


create = OmniCreate()

print(create.Search_Insert_Index([1, 3, 5, 6], 5))
