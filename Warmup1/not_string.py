def not_string(str):
    if "not" in str[0:3]:
        return str
    else:
        return "not " + str