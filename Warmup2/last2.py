def last2(str):
    if len(str) <= 2:
        return 0
    last_two = str[len(str)-2:]
    counter = 0
    for i in range(len(str)):
        if str[i:i+2] == last_two:
            counter += 1
    return counter-1

