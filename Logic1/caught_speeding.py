def caught_speeding(speed, is_birthday):
    if is_birthday:
        high = 86
        med = 66
    else:
        high = 81
        med = 61
    if speed >= high:
        return 2
    elif speed >= med:
        return 1
    return 0
