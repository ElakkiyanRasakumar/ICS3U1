def cat_dog(str):
    dog = str.count("dog")
    cat = str.count("cat")
    if dog == cat:
        return True
    else:
        return False