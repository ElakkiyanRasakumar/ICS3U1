def string_bits(str):
    final_sting = ""
    for i in range(len(str)):
        if not i % 2:
            final_sting += str[i]
    return final_sting