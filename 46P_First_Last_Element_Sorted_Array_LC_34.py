class OmniCreate:
    def searchRange(self, nums, target):

        print(nums)

        output = []

        left, right = 0, len(nums)-1
        middle = (right - left)//2

        while left <= right:

            # print(left)
            # print(right)
            # print(middle)
            # print(nums[middle])
            # print(target)
        
            if nums[middle] == target:
                output.append(middle)
                left = middle + 1             
            elif target > nums[middle]:
                left = middle + 1
            elif target < nums[middle]:
                right = middle - 1

            middle = left + (right - left)//2
  
        return output
            


create = OmniCreate()

print(create.searchRange([5,7,7,8,8,10], 8))