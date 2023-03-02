def sum13(nums):
    sum = 0
    for i in range(len(nums)):
        if nums[i-1] == 13:
            print(sum)
            continue
        if nums[i] == 13:
            print(sum)
            continue

        sum += nums[i]
    print(sum)
    return sum

sum13([1, 2 , 2, 1, 13])