def string_splosion(str):
    final_string = ""
    for i in range(len(str)):
        final_string += str[0:i]
    #final_string += str
    return final_string + str