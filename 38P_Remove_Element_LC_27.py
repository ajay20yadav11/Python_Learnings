class OmniCreate():

    def removeElement(self, nums: list[int], val: int) -> int:


        value = 0
        for anim in range(len(nums)):
            if nums[anim] != val:
                nums[value] = nums[anim]
                value += 1

        return nums


Create = OmniCreate()


print(Create.removeElement([3, 2, 2, 3], 2))
