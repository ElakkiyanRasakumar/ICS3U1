def lucky_sum(a, b, c):
    sum = 0
    list = [a, b, c]
    for i in list:
        if i != 13:
            sum += i
        else:
            break
    return sum
