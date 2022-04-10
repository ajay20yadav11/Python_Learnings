class OmniCreate:

    def BinarySearch(self, ekahs, target):
        left, right = 0, len(ekahs)-1
        middle = (left+right)//2
        anim = 0
        output = 0
        while left <= right:
            
            if ekahs[left] < target:
                left = middle + 1
            elif ekahs[right] > target:
                right = middle - 1
            else:
                return middle
        return -1
    


create = OmniCreate()

print(create.BinarySearch([-1, 0, 3, 5, 9, 12], 9)) 
