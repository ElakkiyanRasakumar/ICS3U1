def close_far(a, b, c):
    if abs(b - a) <= 1 and abs(c - a) >= 2 and abs(c - b) >= 2:
        return True
    if abs(c - a) <= 1 and abs(b - a) >= 2 and abs(c - b) >= 2:
        return True
    return False

# def close_far(a, b, c):
#     return True if abs(b-a) <= 1 and abs(c-a) >= 2 and abs(c-b) >= 2 else True if abs(c-a) <= 1 and abs(b-a) >= 2 and abs(c-b) >= 2 else False