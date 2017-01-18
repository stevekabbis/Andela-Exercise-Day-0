def find_max_min(numbers):
    min_max = []
    max_num = max(numbers)
    min_num = min(numbers)

    if isinstance(numbers, list):
        if max_num==min_num:
            min_max.append(max_num)
            return min_max
        else:
            min_max.append(min_num)
            min_max.append(max_num)
            return min_max

    else:
        return None
