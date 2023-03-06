def count_evens(nums):
    counter = 0
    for i in nums:
        if not i % 2:
            counter += 1
    return counter