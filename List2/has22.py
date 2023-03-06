def has22(nums):
    for i in range(len(nums)):
        if nums[i] == 2 and nums[i-1] == 2 and i != 0:
            return True
    else:
        return False