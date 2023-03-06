def centered_average(nums):
    value = 0
    for i in range(len(nums)):
        value += nums[i]
    value = (value - max(nums) - min(nums))//(len(nums)-2)
    return value