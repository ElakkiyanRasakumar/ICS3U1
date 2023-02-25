def array_count9(nums):
    counter = 0
    for i in nums:
        if i == 9:
            counter += 1
    return counter