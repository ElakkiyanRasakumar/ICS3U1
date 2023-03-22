def lone_sum(a, b, c):
    list = [a, b, c]
    final_list = []
    for i in list:
        if i not in final_list and list.count(i) <= 1 :
            final_list.append(i)
    return sum(final_list)

