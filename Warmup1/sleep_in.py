def sleep_in(weekday, vacation):
    if not weekday:
        return True
    if weekday and not vacation:
        return False
    else:
        return True
