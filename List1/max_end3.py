def max_end3(nums):
    for i in range(len(nums)):
        if nums[0] > nums[-1]:
            nums[i] = nums[0]
        else:
            nums[i] = nums[-1]
    return nums
