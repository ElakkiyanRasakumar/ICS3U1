def make_bricks(small, big, goal):
    if small + big * 5 >= goal:
        if goal % 5 <= small:
            return True
        else:
            return False
    else:
        return False
