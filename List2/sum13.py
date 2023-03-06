def sum13(nums):
    sum = 0
    if len(nums) == 0:
        return 0
    for i in range(len(nums)):
      if i != 0:
        if nums[i-1] == 13:
            continue
      if nums[i] == 13:
        continue
      else:
        sum += nums[i]

    return sum