def remove_duplicate(nums):

    total_poped = 0

    index_to_tra = 0
    last_element = len(nums)
    cond = True

    while index_to_tra < last_element:
    
        while cond:
            if nums[index_to_tra] in nums[index_to_tra+1:]:

                nums.pop(index_to_tra)
                total_poped += 1
            else:
                cond = False
        
        cond = True
        
        index_to_tra += 1
        last_element = len(nums)

    for anim in range(0, total_poped):
        nums.append(0)

    
    return nums



animated = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

print(remove_duplicate(animated))