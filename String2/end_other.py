def end_other(a, b):
    a = a.lower()
    b = b.lower()

    if a in b[len(b) - len(a):len(b)]:
        return True
    if b in a[len(a) - len(b):len(a)]:
        return True
    else:
        return False