#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None

    result = []
    for value in my_list:
        result.append(True) if value % 2 == 0 else result.append(False)
    return result
