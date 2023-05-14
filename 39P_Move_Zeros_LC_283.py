class OmniCreate:
    def moveZeros(self, nums: list[int]):
        new_val = 0
        for anim in range(len(nums)):
            if nums[anim] != 0:
                new_num = nums.pop(anim)
                nums.insert(new_val, new_num)
                new_val += 1

        return nums


create = OmniCreate()

print(create.moveZeros([0, 0, 1, 1, 0, 0, 0, 1, 1, 1]))
