def sum67(nums):
    counter = 0
    count = True
    for i in range(len(nums)):
        if nums[i] == 6:
            count = False
        if nums[i] == 7 and not count:
            count = True
        elif count:
            counter += nums [i]
    return counter
